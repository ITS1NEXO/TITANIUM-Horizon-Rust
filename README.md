# TITANIUM — Minecraft Dressing Room Mod

**Creator:** ZYVIX  
**Project:** TITANIUM  
**Target:** Horizon Rust  
**Mod category:** Dressing Room  
**Planned package formats:** `.hnmod` and `.hmod`

## Overview

TITANIUM is a Minecraft Dressing Room mod for Horizon Rust. Its purpose is to extend or customize the Dressing Room experience rather than act as an FPS-optimization mod.

TITANIUM is developed independently. The separate HorizDroid project has been discontinued; TITANIUM does not depend on HorizDroid.

## Package formats

The project targets both Horizon mod package formats:

- **`.hmod`** — content-mod package.
- **`.hnmod`** — native-mod package.

The two formats are separate build outputs. A successful build must package each format according to its own supported manifest, contents, and compatibility requirements; simply renaming one archive is not valid format conversion.

## Current status

The repository previously contained an API 0.2 `.hmod` compatibility foundation. That foundation is not, by itself, a completed Dressing Room implementation, and it does not establish that a working `.hnmod` build is available.

The Dressing Room feature set and format-specific packaging still need implementation and validation against the target Horizon Rust build.

## Build and validation

Build artifacts should be produced independently for `.hmod` and `.hnmod`. Each output must pass its corresponding format checks and be tested in Horizon Rust before being described as supported.

Do not treat a successful ZIP/package step as proof that the mod loads or that its Dressing Room features work in-game.

## Development goals

1. Implement the intended Dressing Room features.
2. Build a valid `.hmod` package.
3. Build a valid `.hnmod` package.
4. Validate both packages against their respective format requirements.
5. Test both outputs in Horizon Rust and document verified compatibility.

## Credits

Created by **ZYVIX**.

TITANIUM is an unofficial community project and is not affiliated with or endorsed by Mojang or Microsoft.
