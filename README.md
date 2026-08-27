# PlayTorrio — Unofficial AltStore Source

[![AltStore source](https://img.shields.io/badge/AltStore-source-6030A8)](playtorrio-ios.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![iOS apps](https://img.shields.io/badge/iOS-PlayTorrio%20V3%20%2B%20Legacy-6030A8)](playtorrio-ios.json)

An **unofficial, community-maintained AltStore-format source** for [PlayTorrio](https://playtorrio.xyz/) on iPhone and iPad. It works with signing apps that consume the standard AltStore source format, including AltStore, SideStore, Feather, ESign, Scarlet, and Sideloadly.

IPAs are downloaded directly from PlayTorrio's public GitHub releases. This repository only publishes source metadata and is not affiliated with or supported by the PlayTorrio developer.

## Quick start

### One-tap install

Open the installation page on your iPhone or iPad:

[**Add PlayTorrio source →**](https://namillis.github.io/playtorrio-altstore/install.html)

The page can open the source directly in AltStore or SideStore. It also provides a copy button for Feather, ESign, Scarlet, and other signing apps.

### Add the source manually

After GitHub Pages is enabled, paste this URL into your signing app's **Sources** or **Repositories** section:

```text
https://namillis.github.io/playtorrio-altstore/playtorrio-ios.json
```

If Pages is not enabled yet, use the raw GitHub fallback:

```text
https://raw.githubusercontent.com/namillis/playtorrio-altstore/main/playtorrio-ios.json
```

Once added, choose PlayTorrio V3 or PlayTorrio Legacy and install the desired version.

## Available apps

| App | Bundle identifier | Latest version | Minimum iOS | Upstream |
|---|---|---:|---:|---|
| PlayTorrio V3 | `com.example.playtorrio` | 1.0.0 (build 1) | 14.0 | [PlayTorrioV3](https://github.com/ayman708-UX/PlayTorrioV3/releases) |
| PlayTorrio Legacy | `com.playtorrio.app` | 1.4.0 (build 41) | 13.0 | [PlayTorrioV2](https://github.com/ayman708-UX/PlayTorrioV2/releases) |

### Why are V3 and Legacy separate apps?

The V3 IPA uses a different bundle identifier from V2. iOS therefore treats V3 as a separate application rather than an update to the legacy app. Keeping two source entries accurately represents the packages and lets existing V2 users retain access to the older releases.

## Metadata verification

Published metadata is read directly from each IPA's main `Info.plist`, including:

- Bundle identifier
- Marketing version and build number
- Minimum supported iOS version
- iPhone and iPad device support
- Download size
- SHA-256 integrity hash

The source uses version-pinned GitHub release URLs so a future release cannot silently change an older entry's file, size, or hash.

## Hosting with GitHub Pages

The raw GitHub fallback works immediately. GitHub Pages is preferred because it hosts the one-tap installation page and serves the source with an `application/json` content type.

1. Open **Settings → Pages** in this repository.
2. Select **Deploy from a branch**.
3. Choose `main` and `/ (root)`.
4. Save and wait for GitHub Pages to deploy.

The page will be available at:

```text
https://namillis.github.io/playtorrio-altstore/install.html
```

## Repository contents

```text
playtorrio-altstore/
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
- [Feather](https://github.com/khcrysalis/Feather)

## License and attribution

This metadata repository is licensed under the [MIT License](LICENSE).

PlayTorrio belongs to its respective developer. AltStore and SideStore belong to their respective projects. Their names and assets are used only to identify compatibility and upstream downloads.
