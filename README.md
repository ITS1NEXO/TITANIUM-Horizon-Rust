# TITANIUM — Horizon Rust Skin Customizer

**Creator:** ZYVIX  
**Target:** Horizon Rust (Minecraft: Java Edition rewritten in Rust)  
**Purpose:** Local player-skin importing, previewing and switching  
**Planned outputs:** `.hnmod` native mod and an optional `.hmod` content pack

## Overview

TITANIUM is an independent Horizon Rust mod project focused on a Dressing Room-style skin customizer. It is not a Bedrock add-on and does not use Bedrock's Dressing Room APIs.

HorizDroid has been discontinued. TITANIUM continues independently and does not depend on HorizDroid.

## Planned skin features

- Import a local Minecraft skin PNG.
- Preview the selected skin before applying it.
- Select the player model: **Classic (4-pixel arms)** or **Slim (3-pixel arms)**.
- Save imported skins locally and switch between saved skins.
- Keep the selected skin and model choice between game sessions.

These are project goals, not claims about features already implemented.

## Horizon package architecture

Horizon has two distinct mod formats:

- **`.hnmod` — Native mod:** Rust code that adds behaviour and can hook into the game. This is the required format for a skin importer, UI, local file handling and player-render integration.
- **`.hmod` — Content mod:** Data and assets only. It cannot implement the importer or change game behaviour by itself. It may be used for optional bundled assets if TITANIUM needs them.

The formats are not interchangeable. A package must be built and validated using the correct tooling; renaming an archive is not conversion.

Horizon exposes a native player-render hook that allows a mod to draw a player's model itself. That is a possible rendering integration point, but it is not a ready-made skin-import API. TITANIUM still needs to implement and test PNG handling, model geometry/UV mapping, preview UI, persistence and rendering against the target Horizon revision.

## Current status

The repository currently contains only an early API 0.2 content-mod packaging foundation. It does **not** yet contain the skin importer, a native-mod implementation, or a verified in-game Dressing Room UI.

The existing `.hmod` artifact is therefore a packaging foundation only, not a usable skin customizer. A working `.hnmod` has not yet been built.

## Development milestones

1. Establish the native-mod template and pin a tested Horizon revision.
2. Implement PNG validation and local skin-library storage.
3. Implement Classic and Slim model selection and skin preview.
4. Integrate the custom skin with the player renderer, without claiming support until tested.
5. Build and validate the `.hnmod` with Horizon's native-mod tooling.
6. Keep a separate `.hmod` output only if TITANIUM has actual content assets to package.
7. Test in Horizon Rust and document the exact supported build.

## Build and validation

A successful archive/package step is not proof that a mod loads or works in-game. Each format must pass its own checks, and skin import/rendering must be tested in Horizon before being marked supported.

## Credits

Created by **ZYVIX**.

TITANIUM is an unofficial community project and is not affiliated with or endorsed by Mojang or Microsoft.
