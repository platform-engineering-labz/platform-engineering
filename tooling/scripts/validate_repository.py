#!/usr/bin/env python3
"""Validate local Markdown links and image references in this repository using Python's stdlib."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
REQUIRED = ("README.md", "AGENTS.md", "engineering-reference/INDEX.md")


def markdown_links(path: Path):
    fence_char = None
    fence_len = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if fence_char is None:
                fence_char, fence_len = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_len:
                fence_char, fence_len = None, 0
            continue
        if fence_char is not None:
            continue
        # The link scanner is intentionally simple; ignore inline code spans.
        without_inline_code = re.sub(r"`[^`]*`", "", line)
        for match in LINK.finditer(without_inline_code):
            yield match.group(1).strip().split(" \"", 1)[0].strip("<>")


def main() -> int:
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"Required file missing: {name}")
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts:
            continue
        for link in markdown_links(file):
            if not link or link.startswith("#") or link.startswith("//"):
                continue
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            local = unquote(parsed.path)
            if not local:
                continue
            target = (ROOT / local.lstrip("/")) if local.startswith("/") else (file.parent / local)
            if not target.exists():
                errors.append(f"{file.relative_to(ROOT)}: broken link {link}")
    if errors:
        print("\n".join(errors))
        return 1
    print("Repository layout and local Markdown links: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
