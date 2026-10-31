#!/usr/bin/env python3
"""Structural and contract validator for Good Calls skills."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS: list[str] = [
    "## When not to use",
    "## Inputs and authorization",
    "## Method",
]
CLOSING_SECTIONS: list[str] = [
    "## Validate and report",
    "## Stopping and persistence",
]
ALLOWED_ENTRIES: set[str] = {
    "SKILL.md",
    "references",
    "templates",
    "scripts",
    "agents",
}
WORD_BUDGET: int = 520

ONES: list[str] = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
TENS: list[str] = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
CN_DIGITS: list[str] = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]


def english_number(n: int) -> str:
    if n < 20:
        return ONES[n]
    tens_idx = n // 10
    ones_idx = n % 10
    return f"{TENS[tens_idx]}-{ONES[ones_idx]}" if ones_idx else TENS[tens_idx]


def chinese_number(n: int) -> str:
    if n < 10:
        return CN_DIGITS[n]
    tens_idx = n // 10
    ones_idx = n % 10
    head = "十" if tens_idx == 1 else f"{CN_DIGITS[tens_idx]}十"
    return f"{head}{CN_DIGITS[ones_idx]}" if ones_idx else head


def markdown_files(path: Path) -> list[Path]:
    if not path.is_dir():
        return [path] if path.suffix == ".md" else []
    return sorted(p for p in path.rglob("*.md") if p.is_file())


def link_targets(text: str) -> list[str]:
    pattern = re.compile(r"\]\(([^)]+)\)")
    return [m.strip("<> \t\n") for m in pattern.findall(text)]


def is_relative_link(target: str) -> bool:
    if re.match(r"^(https?:|mailto:|#|/)", target):
        return False
    return not any(char in target for char in ("<", ">", "*"))


class SuiteChecker:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.errors: list[tuple[str, str, str, str]] = []
        self.warnings: list[tuple[str, str, str, str]] = []

    def err(self, code: str, file_path: Path, msg: str, fix: str) -> None:
        try:
            rel = file_path.relative_to(self.root).as_posix()
        except ValueError:
            rel = file_path.as_posix()
        self.errors.append((code, rel, msg, fix))

    def warn(self, code: str, file_path: Path, msg: str, fix: str) -> None:
        try:
            rel = file_path.relative_to(self.root).as_posix()
        except ValueError:
            rel = file_path.as_posix()
        self.warnings.append((code, rel, msg, fix))

    def check_links(self, target: Path) -> None:
        if not target.exists():
            return
        files = markdown_files(target)
        for f in files:
            text = f.read_text(encoding="utf-8")
            for t in link_targets(text):
                if not is_relative_link(t):
                    continue
                clean = t.split("#")[0]
                if not clean:
                    continue
                dest = (f.parent / clean).resolve()
                if not dest.exists():
                    self.err(
                        "LINK_BROKEN",
                        f,
                        f"link target not found: {t}",
                        "Fix the path or remove the link.",
                    )

    def check_skill(self, name: str) -> None:
        skill_dir = self.root / "skills" / name
        skill_file = skill_dir / "SKILL.md"
        text = skill_file.read_text(encoding="utf-8")
        lines = text.splitlines()

        # Frontmatter
        if not lines or lines[0] != "---":
            self.err(
                "FRONTMATTER_MISSING",
                skill_file,
                "missing YAML frontmatter block",
                "Start with ---.",
            )
            return

        try:
            fm_end = lines.index("---", 1)
        except ValueError:
            self.err(
                "FRONTMATTER_MISSING",
                skill_file,
                "missing YAML frontmatter close",
                "Close frontmatter with ---.",
            )
            return

        fm_lines = lines[1:fm_end]
        fm_name = ""
        fm_desc = ""
        user_only = False

        for l in fm_lines:
            if l.startswith("name:"):
                fm_name = l.split(":", 1)[1].strip()
            elif l.startswith("description:"):
                fm_desc = l.split(":", 1)[1].strip()
            elif l.strip() == "disable-model-invocation: true":
                user_only = True

        if not fm_name:
            self.err(
                "NAME_MISSING",
                skill_file,
                "frontmatter name is missing",
                f"Add name: {name}.",
            )
        else:
            if fm_name != name:
                self.err(
                    "NAME_MISMATCH",
                    skill_file,
                    f"name {fm_name} must match directory {name}",
                    f"Set name: {name}.",
                )
            if not re.match(r"^[a-z0-9-]+$", fm_name):
                self.err(
                    "NAME_INVALID",
                    skill_file,
                    f"name {fm_name} has invalid characters",
                    "Use lowercase and hyphens.",
                )

        if not fm_desc:
            self.err(
                "DESCRIPTION_MISSING",
                skill_file,
                "frontmatter description is missing",
                "Add triggering conditions.",
            )
        elif not re.match(r"^Use (when|for)\b", fm_desc):
            self.warn(
                "DESCRIPTION_TRIGGER",
                skill_file,
                f"description should start with Use when or Use for: {fm_desc[:60]}",
                "Start with Use when/for.",
            )

        # Required sections order
        def line_idx(h: str) -> int:
            for idx, line in enumerate(lines):
                if line.strip() == h:
                    return idx
            return -1

        prev = -1
        for req in REQUIRED_SECTIONS:
            idx = line_idx(req)
            if idx < 0:
                self.err(
                    "SECTION_MISSING",
                    skill_file,
                    f"missing required section {req}",
                    f"Add {req}.",
                )
                continue
            if idx < prev:
                self.err(
                    "SECTION_ORDER",
                    skill_file,
                    f"{req} must come after previous required section",
                    "Reorder sections.",
                )
            prev = idx

        closing_indices = [
            (c, line_idx(c)) for c in CLOSING_SECTIONS if line_idx(c) >= 0
        ]
        if not closing_indices:
            self.err(
                "SECTION_MISSING",
                skill_file,
                f"missing closing section: {' or '.join(CLOSING_SECTIONS)}",
                "Add closing section.",
            )
        elif min(idx for _, idx in closing_indices) < prev:
            self.err(
                "SECTION_ORDER",
                skill_file,
                "closing section must come last",
                "Move to end.",
            )

        # Disallowed elements
        if any(l.strip() == "## When to use" for l in lines):
            self.err(
                "WHEN_TO_USE_PRESENT",
                skill_file,
                "When to use section duplicates description",
                "Remove section.",
            )
        if "\u2014" in text:
            self.err(
                "EM_DASH",
                skill_file,
                "em dash is not allowed",
                "Use colon, comma, or parentheses.",
            )
        for legacy in (".agents/notes", ".agents/work"):
            if legacy in text:
                self.err(
                    "LEGACY_PATH",
                    skill_file,
                    f"legacy path {legacy}",
                    "Use docs/agents/... instead.",
                )

        # Word budget check
        words = len(text.split())
        has_ref = (skill_dir / "references").is_dir()
        if words > WORD_BUDGET and not has_ref:
            self.warn(
                "WORD_BUDGET",
                skill_file,
                f"{words} words with no references/ directory",
                "Move detail to references/.",
            )

        # Entries in skill directory
        for entry in skill_dir.iterdir():
            if entry.name not in ALLOWED_ENTRIES:
                self.err(
                    "SKILL_DIR_ENTRY",
                    entry,
                    f"unexpected entry {entry.name} in skill directory",
                    "Allowed: SKILL.md, references/, templates/, scripts/, agents/.",
                )

        agents_dir = skill_dir / "agents"
        if agents_dir.is_dir():
            for entry in agents_dir.iterdir():
                if entry.name != "openai.yaml":
                    self.err(
                        "SKILL_DIR_ENTRY",
                        entry,
                        f"unexpected entry {entry.name} under agents/",
                        "Only openai.yaml allowed.",
                    )

        has_openai = (agents_dir / "openai.yaml").exists()
        if user_only and not has_openai:
            self.err(
                "USER_ONLY_MISMATCH",
                skill_file,
                "disable-model-invocation requires agents/openai.yaml",
                "Add agents/openai.yaml.",
            )
        elif not user_only and has_openai:
            self.err(
                "USER_ONLY_MISMATCH",
                skill_file,
                "agents/openai.yaml requires disable-model-invocation: true",
                "Add flag or remove file.",
            )

        # Resource links
        all_skill_text = "\n".join(
            f.read_text(encoding="utf-8") for f in markdown_files(skill_dir)
        )
        for sub in ("references", "templates"):
            subdir = skill_dir / sub
            if not subdir.is_dir():
                continue
            for entry in subdir.iterdir():
                rel_resource = f"{sub}/{entry.name}"
                if rel_resource not in all_skill_text:
                    self.warn(
                        "RESOURCE_UNLINKED",
                        entry,
                        f"resource {rel_resource} is not referenced in Markdown",
                        "Link from SKILL.md or references.",
                    )

        self.check_links(skill_dir)

    def check_readmes(self, names: list[str]) -> None:
        expect = set(names)
        n = len(names)
        specs = [("README.md", False), ("README_zh-CN.md", True)]

        for filename, is_zh in specs:
            readme_path = self.root / filename
            if not readme_path.exists():
                self.err(
                    "README_MISSING", readme_path, f"{filename} not found", "Add it."
                )
                continue

            content = readme_path.read_text(encoding="utf-8")
            found: set[str] = set(
                re.findall(r"\]\(skills/([a-z0-9-]+)/SKILL\.md\)", content)
            )

            for x in expect:
                if x not in found:
                    self.err(
                        "README_MISSING_SKILL",
                        readme_path,
                        f"{filename} has no catalog row for {x}",
                        f"Add row linking skills/{x}/SKILL.md.",
                    )
            for x in found:
                if x not in expect:
                    self.err(
                        "README_UNKNOWN_SKILL",
                        readme_path,
                        f"{filename} lists unknown skill {x}",
                        "Remove row or add skill.",
                    )

            token = (
                f"{chinese_number(n)}个独立技能"
                if is_zh
                else f"{english_number(n)} independent skills"
            )
            if token not in content:
                self.err(
                    "README_COUNT",
                    readme_path,
                    f"{filename} must state {token}",
                    f"Update skill count to {n}.",
                )

    def check_all(
        self,
    ) -> tuple[list[tuple[str, str, str, str]], list[tuple[str, str, str, str]]]:
        skills_dir = self.root / "skills"
        if not skills_dir.is_dir():
            self.err(
                "SKILLS_DIR_MISSING",
                skills_dir,
                "skills/ directory not found",
                "Create skills/.",
            )
            return self.errors, self.warnings

        names: list[str] = []
        for entry in skills_dir.iterdir():
            if not entry.is_dir():
                self.err(
                    "SKILLS_DIR_ENTRY",
                    entry,
                    f"unexpected entry {entry.name} under skills/",
                    "Move into a skill or remove.",
                )
                continue
            if not (entry / "SKILL.md").exists():
                self.err(
                    "SKILL_MISSING",
                    entry,
                    f"skills/{entry.name}/ has no SKILL.md",
                    f"Add skills/{entry.name}/SKILL.md.",
                )
                continue
            names.append(entry.name)

        names.sort()

        for name in names:
            self.check_skill(name)

        self.check_links(self.root / "docs")
        self.check_links(self.root / "README.md")
        self.check_links(self.root / "README_zh-CN.md")
        self.check_readmes(names)

        return self.errors, self.warnings


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate Good Calls skills suite structure and contracts."
    )
    parser.add_argument("path", nargs="?", default=".", help="Root repository path")
    args = parser.parse_args()

    checker = SuiteChecker(Path(args.path))
    errors, warnings = checker.check_all()

    for code, path, msg, fix in warnings:
        print(f"warning {code}: {path}: {msg}\n  fix: {fix}", file=sys.stderr)

    if errors:
        print(
            f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr
        )
        for code, path, msg, fix in errors:
            print(f"error {code}: {path}: {msg}\n  fix: {fix}", file=sys.stderr)
        sys.exit(1)

    print(f"OK: 0 error(s), {len(warnings)} warning(s)")
    sys.exit(0)


if __name__ == "__main__":
    main()
