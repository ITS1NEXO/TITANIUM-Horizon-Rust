# TITANIUM — Horizon Performance

**Creator:** ZYVIX  
**Target:** Horizon `.hmod` content-mod format (API 0.2)  
**Package ID:** `titanium`

## Current status

This repository starts with a verified-format foundation and an automated `.hmod` packaging workflow. It is **not yet an FPS optimization mod**.

Horizon API 0.2 content mods are data-only. They can add supported blocks, items, recipes, loot, tags, models and textures in the mod's own namespace. They cannot run code or directly change the renderer, frame pacing, existing particle systems, or game performance settings.

Because this project is intentionally `.hmod`-only for compatibility with the target Android launcher, those engine-level optimizations are out of scope unless that launcher later supports a suitable code-mod API.

## Build

GitHub Actions packages the repository's `horizon-mod.toml`, `assets/` and `data/` into `TITANIUM-0.1.0.hmod` and uploads it as an artifact.

The workflow checks the manifest and archive structure. This is a packaging check, **not proof that every Horizon build or unofficial Android fork can load the mod**.

## Compatibility

- Manifest API: `0.2`
- Format: ZIP-based `.hmod`
- Code/WASM: none
- Native `.hnmod`: not used

Official references:
- https://playhorizon.dev/docs/content-mods
- https://github.com/horizon-rust/horizon/blob/main/docs/mods.md

## Roadmap

1. Confirm that the target Android Horizon fork accepts API 0.2 content mods.
2. Identify a useful, supported content-only feature before adding assets or data.
3. Test the resulting artifact in the target launcher.
4. Only describe performance benefits if an actual before/after test demonstrates them.
