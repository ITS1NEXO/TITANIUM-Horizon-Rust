#!/usr/bin/env python3
"""Create Horizon's source-only .hnmod package for TITANIUM."""
import hashlib
import json
from pathlib import Path
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
GAME = "26.3"

def main():
    compat = json.loads((ROOT / "compatibility.json").read_text())
    manifest_path = ROOT / "mixins/titanium/horizon-mixin.toml"
    manifest = tomllib.loads(manifest_path.read_text())
    mod = manifest["mod"]
    if mod["id"] != "titanium":
        raise SystemExit("unexpected native mod id")
    if manifest["compatibility"]["horizon_revision"] != compat["horizon_revision"]:
        raise SystemExit("Horizon revision mismatch")
    native = {
        "schema": 1,
        "id": mod["id"],
        "version": mod["version"],
        "game": GAME,
        "horizon": compat["horizon_revision"],
        "mixins": compat["horizon_mixins_revision"],
    }
    files = {
        "horizon-native.json": (json.dumps(native, indent=2, sort_keys=True) + "\n").encode(),
        "mixins/titanium/horizon-mixin.toml": manifest_path.read_bytes(),
        "mixins/titanium/runtime.rs": (ROOT / "mixins/titanium/runtime.rs").read_bytes(),
    }
    out = ROOT / "dist" / f"titanium-{mod['version']}.hnmod"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"Created {out} ({out.stat().st_size} bytes)")
    print(f"SHA-256: {digest}")

if __name__ == "__main__":
    main()
