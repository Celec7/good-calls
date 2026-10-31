#!/usr/bin/env python3
"""Validate Architecture Decision Record (ADR) file format and lifecycle consistency."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

STATUS_PATTERN = re.compile(
    r"^\*\*Status:\*\*\s+(proposed|implemented|rejected|archived)(?:\s*:\s*.+)?$",
    re.IGNORECASE,
)
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")

REQUIRED_SECTIONS: dict[str, list[str]] = {
    "proposed": ["## Problem", "## Proposal", "## Alternatives considered"],
    "implemented": [
        "## Problem",
        "## Decision",
        "## Alternatives considered",
        "## Consequences",
    ],
    "rejected": ["## Problem", "## Proposal"],
}

BANNED_IN_IMPLEMENTED = re.compile(
    r"^##\s+(?:Proposal\b|Plan\b|Migration plan\b|Acceptance criteria\b)", re.IGNORECASE
)


def validate_note(file_path: Path, lifecycle: str) -> list[str]:
    errors: list[str] = []
    rel_path = file_path.as_posix()

    if not DATE_PATTERN.match(file_path.name):
        errors.append(f"{rel_path}: filename must follow YYYY-MM-DD-topic.md")

    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Filter out code fences for heading checks
    in_fence = False
    prose_lines: list[str] = []
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            prose_lines.append(line)

    headings = [line.strip() for line in prose_lines if line.strip().startswith("#")]
    h1s = [h for h in headings if h.startswith("# ") and not h.startswith("## ")]
    h2s = [h for h in headings if h.startswith("## ")]

    if not h1s:
        errors.append(f"{rel_path}: missing top-level # title")

    # Status validation
    status_matches = [line for line in prose_lines if "**Status:**" in line]
    if not status_matches:
        errors.append(f"{rel_path}: missing **Status:** line")
    else:
        status_line = status_matches[0].strip()
        m = STATUS_PATTERN.match(status_line)
        if not m:
            errors.append(f"{rel_path}: invalid status line format: {status_line}")
        elif lifecycle in ("proposed", "implemented", "rejected"):
            actual_status = m.group(1).lower()
            if actual_status != lifecycle:
                errors.append(
                    f"{rel_path}: status '{actual_status}' does not match directory '{lifecycle}'"
                )

    # Heading checks
    if h2s:
        if h2s[0] != "## Problem":
            errors.append(
                f"{rel_path}: first section must be '## Problem' (got '{h2s[0]}')"
            )
    else:
        errors.append(f"{rel_path}: no ## sections found")

    for req in REQUIRED_SECTIONS.get(lifecycle, []):
        if not any(h.lower() == req.lower() for h in h2s):
            errors.append(f"{rel_path}: missing required section '{req}'")

    if lifecycle == "implemented":
        for h in h2s:
            if BANNED_IN_IMPLEMENTED.match(h):
                errors.append(
                    f"{rel_path}: '{h}' is a proposal-era section; fold into Decision/Consequences"
                )

    return errors


def check_notes(root_dir: Path) -> int:
    notes_dir = root_dir / "docs" / "agents" / "notes"
    if not notes_dir.exists():
        notes_dir = root_dir

    if not notes_dir.exists():
        print(f"Directory not found: {notes_dir}", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    checked_count = 0

    for lifecycle in ("proposed", "implemented", "rejected"):
        dir_path = notes_dir / lifecycle
        if not dir_path.is_dir():
            continue
        for note_file in dir_path.glob("*.md"):
            checked_count += 1
            all_errors.extend(validate_note(note_file, lifecycle))

    if all_errors:
        print(
            f"ADR format check failed with {len(all_errors)} error(s):", file=sys.stderr
        )
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: {checked_count} ADR(s) checked, 0 errors.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate ADR formatting and lifecycle status."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root repository directory or notes directory",
    )
    args = parser.parse_args()

    sys.exit(check_notes(Path(args.path)))


if __name__ == "__main__":
    main()
