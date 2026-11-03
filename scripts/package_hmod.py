#!/usr/bin/env python3
"""Validate and package a Horizon API 0.2 content mod."""
from pathlib import Path
import sys
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "horizon-mod.toml"
OUT = ROOT / "dist" / "TITANIUM-0.1.0.hmod"

def main() -> int:
    if not MANIFEST.is_file():
        raise SystemExit("ERROR: horizon-mod.toml is missing")
    with MANIFEST.open("rb") as stream:
        manifest = tomllib.load(stream)

    required = {"id", "name", "version", "description", "authors", "api", "side", "capabilities"}
    missing = sorted(required - manifest.keys())
    if missing:
        raise SystemExit(f"ERROR: manifest missing keys: {', '.join(missing)}")
    if manifest["id"] != "titanium" or manifest["api"] != "0.2":
        raise SystemExit("ERROR: expected TITANIUM manifest with content API 0.2")
    if manifest["side"] != "both" or "registries" not in manifest["capabilities"]:
        raise SystemExit("ERROR: invalid content-mod side or capabilities")

    entries = [MANIFEST]
    for folder_name in ("assets", "data"):
        folder = ROOT / folder_name
        if folder.exists():
            entries.extend(p for p in folder.rglob("*") if p.is_file())

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(entries):
            archive.write(path, path.relative_to(ROOT).as_posix())

    with zipfile.ZipFile(OUT, "r") as archive:
        names = archive.namelist()
        if "horizon-mod.toml" not in names:
            raise SystemExit("ERROR: root manifest missing from archive")
        if any(name.startswith("/") or ".." in Path(name).parts for name in names):
            raise SystemExit("ERROR: unsafe archive path")

    print(f"Created {OUT}")
    print("Structural validation passed; in-game compatibility is not yet verified.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
