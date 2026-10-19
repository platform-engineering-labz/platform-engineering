#!/usr/bin/env python3
"""Stage handbook Markdown and local PNGs without copying repository internals."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / ".site-src"
if DEST.exists():
    shutil.rmtree(DEST)
EXCLUDED = {".git", ".github", ".agents", ".site-src", "node_modules", ".venv", "__pycache__"}
for source in ROOT.rglob("*"):
    if not source.is_file() or source.suffix.lower() not in {".md", ".png"}:
        continue
    relative = source.relative_to(ROOT)
    if any(part in EXCLUDED for part in relative.parts):
        continue
    target = DEST / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
print(f"Staged handbook content at {DEST}")
