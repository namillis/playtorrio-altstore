from __future__ import annotations

import copy
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import update_playtorrio as updater


ROOT = Path(__file__).resolve().parents[1]


class UpdatePlayTorrioTest(unittest.TestCase):
    def setUp(self) -> None:
        self.source = json.loads((ROOT / updater.SOURCE_PATH).read_text())
        self.readme = (ROOT / updater.README_PATH).read_text()
        self.release = updater.VerifiedRelease(
            version="9.8.7",
            build_version="987",
            date="2026-08-28",
            notes="Fix playback\nImprove loading",
            caption="Fix playback · Improve loading",
            download_url=(
                "https://github.com/ayman708-UX/PlayTorrioV3/"
                "releases/download/v9.8.7/PlayTorrio-iOS.ipa"
            ),
            size=37_000_000,
            sha256="a" * 64,
            minimum_os_version="15.0",
        )

    def test_current_files_are_consistent(self) -> None:
        updater._validate_cross_file(self.source, self.readme)
        self.assertEqual(self.readme, updater._update_readme(self.readme, self.source))

    def test_apply_release_updates_all_derived_fields(self) -> None:
        source = copy.deepcopy(self.source)

        self.assertTrue(updater._apply_release(source, self.release))
        app, latest = updater._current_v3(source)
        updated_readme = updater._update_readme(self.readme, source)
        updater._validate_cross_file(source, updated_readme)

        self.assertEqual("9.8.7", latest["version"])
        self.assertEqual("987", latest["buildVersion"])
        self.assertEqual(self.release.notes, latest["localizedDescription"])
        self.assertEqual(self.release.download_url, latest["downloadURL"])
        self.assertEqual(self.release.size, latest["size"])
        self.assertEqual(self.release.sha256, latest["sha256"])
        self.assertEqual("15.0", latest["minOSVersion"])
        self.assertEqual(latest["version"], app["version"])
        self.assertEqual(latest["date"], app["versionDate"])
        self.assertEqual(latest["localizedDescription"], app["versionDescription"])
        self.assertEqual(latest["downloadURL"], app["downloadURL"])
        self.assertEqual(latest["size"], app["size"])
        self.assertEqual(latest["minOSVersion"], app["minOSVersion"])
        self.assertEqual("PlayTorrio V3 9.8.7", source["news"][0]["title"])
        self.assertIn("9.8.7 (build 987) | 15.0", updated_readme)

    def test_reapplying_release_is_idempotent(self) -> None:
        source = copy.deepcopy(self.source)
        updater._apply_release(source, self.release)

        self.assertFalse(updater._apply_release(source, self.release))
        app, _ = updater._current_v3(source)
        coordinates = [
            (version["version"], version["buildVersion"]) for version in app["versions"]
        ]
        self.assertEqual(len(coordinates), len(set(coordinates)))

    def test_downgrade_is_rejected(self) -> None:
        older = self.release._replace(version="0.1.0", build_version="1")

        with self.assertRaisesRegex(RuntimeError, "older than source latest"):
            updater._apply_release(copy.deepcopy(self.source), older)

    def test_latest_release_fast_path_skips_download(self) -> None:
        app, latest = updater._current_v3(self.source)
        release = {
            "draft": False,
            "prerelease": False,
            "tag_name": f"v{latest['version']}",
            "published_at": f"{latest['date']}T12:00:00Z",
            "body": latest["localizedDescription"],
            "assets": [
                {
                    "name": updater.IPA_NAME,
                    "size": latest["size"],
                    "digest": f"sha256:{latest['sha256']}",
                    "browser_download_url": latest["downloadURL"],
                }
            ],
        }
        self.assertEqual(latest["version"], app["version"])

        with (
            mock.patch.object(updater, "_gh_api", return_value=release),
            mock.patch.object(updater, "_download_ipa") as download,
        ):
            self.assertIsNone(updater._verify_latest_release(self.source))

        download.assert_not_called()

    def test_atomic_commit_contains_both_files(self) -> None:
        base_commit = "1" * 40
        files = {
            updater.README_PATH: b"readme",
            updater.SOURCE_PATH: b"source",
        }
        calls: list[tuple[str, str, object]] = []
        blob_shas = iter(("2" * 40, "3" * 40))

        def fake_api(endpoint: str, *, method: str = "GET", payload: object = None) -> dict:
            calls.append((endpoint, method, payload))
            if endpoint.endswith(f"git/commits/{base_commit}"):
                return {"tree": {"sha": "4" * 40}}
            if endpoint.endswith("git/blobs"):
                return {"sha": next(blob_shas)}
            if endpoint.endswith("git/trees"):
                paths = [entry["path"] for entry in payload["tree"]]
                self.assertEqual([updater.README_PATH, updater.SOURCE_PATH], paths)
                return {"sha": "5" * 40}
            if endpoint.endswith("git/commits"):
                self.assertEqual([base_commit], payload["parents"])
                return {
                    "sha": "6" * 40,
                    "html_url": f"https://github.com/{updater.SOURCE_REPO}/commit/{'6' * 40}",
                }
            if endpoint.endswith(f"git/ref/heads/{updater.SOURCE_BRANCH}"):
                return {"object": {"sha": base_commit}}
            if endpoint.endswith(f"git/refs/heads/{updater.SOURCE_BRANCH}"):
                self.assertEqual({"sha": "6" * 40, "force": False}, payload)
                return {"object": {"sha": "6" * 40}}
            raise AssertionError(f"unexpected endpoint: {endpoint}")

        with (
            mock.patch.object(updater, "_gh_api", side_effect=fake_api),
            mock.patch.object(updater, "_fetch_file", side_effect=lambda path, _: files[path]),
        ):
            commit_url, commit_sha = updater._commit_files(base_commit, files, "9.8.7")

        self.assertEqual("6" * 40, commit_sha)
        self.assertTrue(commit_url.endswith("6" * 40))
        commit_calls = [call for call in calls if call[0].endswith("git/commits")]
        self.assertEqual(1, len(commit_calls))

    def test_workflow_outputs_reject_multiline_values(self) -> None:
        with tempfile.NamedTemporaryFile() as output:
            with mock.patch.dict(os.environ, {"GITHUB_OUTPUT": output.name}):
                with self.assertRaisesRegex(RuntimeError, "contains a newline"):
                    updater._write_outputs({"changed": "true\nfalse"})


if __name__ == "__main__":
    unittest.main()
