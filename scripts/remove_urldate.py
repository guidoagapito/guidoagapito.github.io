#!/usr/bin/env python3
"""Remove exact BibTeX urldate lines from a .bib file."""

from __future__ import annotations

import argparse
from pathlib import Path


def remove_urldate_lines(file_path: Path, dry_run: bool = False) -> int:
    lines = file_path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept_lines = [line for line in lines if not line.strip().startswith("urldate = {")]
    removed = len(lines) - len(kept_lines)

    if removed > 0 and not dry_run:
        file_path.write_text("".join(kept_lines), encoding="utf-8")

    return removed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Remove all BibTeX urldate lines from a .bib file."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="source/bibliography.bib",
        help="Path to the .bib file (default: source/bibliography.bib)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report how many lines would be removed without modifying the file.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        parser.error(f"File not found: {file_path}")

    removed = remove_urldate_lines(file_path=file_path, dry_run=args.dry_run)

    action = "Would remove" if args.dry_run else "Removed"
    print(f"{action} {removed} line(s) from {file_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
