# PlayTorrio — Unofficial AltStore Source

[![One-tap install](https://img.shields.io/badge/Install-one--tap-6030A8)](https://namillis.github.io/playtorrio-altstore/)
[![AltStore source](https://img.shields.io/badge/AltStore-source-6030A8)](https://namillis.github.io/playtorrio-altstore/playtorrio-ios.json)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-2ea44f)](https://namillis.github.io/playtorrio-altstore/)
[![Update source](https://github.com/namillis/playtorrio-altstore/actions/workflows/source-updater.yml/badge.svg)](https://github.com/namillis/playtorrio-altstore/actions/workflows/source-updater.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![iOS apps](https://img.shields.io/badge/iOS-PlayTorrio%20V3%20%2B%20Legacy-6030A8)](playtorrio-ios.json)

An **unofficial, community-maintained AltStore-format source** for [PlayTorrio](https://playtorrio.xyz/) on iPhone and iPad. It works with signing apps that consume the standard AltStore source format, including AltStore, SideStore, LiveContainer, Scarlet, and Sideloadly.

IPAs are downloaded directly from PlayTorrio's public GitHub releases. This repository only publishes source metadata and is not affiliated with or supported by the PlayTorrio developer.

## Quick start

### One-tap install

Open the live installation page on your iPhone or iPad:

[**Add PlayTorrio source →**](https://namillis.github.io/playtorrio-altstore/)

The page can open the source directly in AltStore, SideStore, or LiveContainer. It also provides a copy button for other signing apps.

### Add the source manually

Paste the live source URL into your signing app's **Sources** or **Repositories** section:

```text
https://namillis.github.io/playtorrio-altstore/playtorrio-ios.json
```

Raw GitHub fallback:

```text
https://raw.githubusercontent.com/namillis/playtorrio-altstore/main/playtorrio-ios.json
```

Once added, choose PlayTorrio V3 or PlayTorrio Legacy and install the desired version.

## Available apps

| App | Bundle identifier | Latest version | Minimum iOS | Upstream |
|---|---|---:|---:|---|
| PlayTorrio V3 | `com.example.playtorrio` | 1.0.8 (build 9) | 14.0 | [PlayTorrioV3](https://github.com/ayman708-UX/PlayTorrioV3/releases) |
| PlayTorrio Legacy | `com.playtorrio.app` | 1.4.0 (build 41) | 13.0 | [PlayTorrioV2](https://github.com/ayman708-UX/PlayTorrioV2/releases) |

### Why are V3 and Legacy separate apps?

The V3 IPA uses a different bundle identifier from V2. iOS therefore treats V3 as a separate application rather than an update to the legacy app. Keeping two source entries accurately represents the packages and lets existing V2 users retain access to the older releases.

## Compatible signing apps

Any signing app that consumes the standard AltStore source format can use this repository. Known-compatible options include:

- **[AltStore Classic](https://altstore.io/)** — the original desktop-paired signer, using AltServer on a Mac or PC
- **[AltStore PAL](https://altstore.io/)** — AltStore's alternative app marketplace for users in the European Union
- **[Scarlet](https://usescarlet.com/)** — an on-device IPA installer
- **[Sideloadly](https://sideloadly.io/)** — a desktop-based sideloader with source support
- **[LiveContainer](https://github.com/LiveContainer/LiveContainer)** — an app launcher that imports and runs compatible IPA files inside a container

Apps that accept a source URL can use the hosted JSON directly. LiveContainer can import the IPA downloaded from a version's release link; its own compatibility limitations still apply.

## Metadata verification

Published metadata is read directly from each IPA's main `Info.plist`, including:

- Bundle identifier
- Marketing version and build number
- Minimum supported iOS version
- iPhone and iPad device support
- Download size
- SHA-256 integrity hash

The source uses version-pinned GitHub release URLs so a future release cannot silently change an older entry's file, size, or hash.

## Live endpoints

GitHub Pages is deployed by the updater workflow and serves both the installation page and source JSON.

| Resource | Live URL |
|---|---|
| One-tap installation page | [namillis.github.io/playtorrio-altstore/](https://namillis.github.io/playtorrio-altstore/) |
| AltStore source JSON | [namillis.github.io/playtorrio-altstore/playtorrio-ios.json](https://namillis.github.io/playtorrio-altstore/playtorrio-ios.json) |
| Raw JSON fallback | [raw.githubusercontent.com/.../playtorrio-ios.json](https://raw.githubusercontent.com/namillis/playtorrio-altstore/main/playtorrio-ios.json) |

GitHub Pages serves the source with an `application/json` content type. Deployments may take up to 10 minutes to propagate through the Pages cache after a merge.

## Repository contents

```text
playtorrio-altstore/
├── .github/workflows/source-updater.yml
├── scripts/
│   ├── test_update_playtorrio.py
│   └── update_playtorrio.py
├── README.md
├── LICENSE
├── install.html
└── playtorrio-ios.json
```

## Limitations

- **Unofficial source:** PlayTorrio does not maintain or support this repository.
- **Sideloading requirements:** You need a compatible signing app and Apple ID.
- **Signature expiry:** Apps signed with a free Apple ID normally expire after 7 days. Paid developer signatures can last up to 1 year.
- **Upstream dependency:** Downloads stop working if PlayTorrio removes or renames its GitHub release assets.
- **Separate V3 installation:** Because the bundle identifier changed, V3 does not install as an in-place update over V2.

## Links

- [PlayTorrio website](https://playtorrio.xyz/)
- [PlayTorrio source code and releases](https://github.com/ayman708-UX/PlayTorrioV3)
- [AltStore](https://altstore.io/)
- [SideStore](https://sidestore.io/)

## License and attribution

This metadata repository is licensed under the [MIT License](LICENSE).

PlayTorrio belongs to its respective developer. AltStore and SideStore belong to their respective projects. Their names and assets are used only to identify compatibility and upstream downloads.
