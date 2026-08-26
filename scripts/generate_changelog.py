#!/usr/bin/env python3
"""Generate content/Changelog.md entries from Git history."""

from __future__ import annotations

import argparse
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import frontmatter


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
CHANGELOG_PATH = CONTENT_DIR / "Changelog.md"
IMAGE_EXTENSIONS = {
    ".avif",
    ".bmp",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".tif",
    ".tiff",
    ".webp",
}
EXCLUDED_EXTENSIONS = IMAGE_EXTENSIONS | {".base", ".pdf"}


@dataclass(frozen=True)
class Change:
    date: str
    status: str
    path: str


def git_output(*args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def display_path(path: str) -> str:
    return path.removeprefix("content/").replace("\\", "/")


def current_content_paths() -> dict[str, str]:
    paths = {}
    for path in CONTENT_DIR.rglob("*"):
        if path.is_file():
            relative = path.relative_to(CONTENT_DIR).as_posix()
            paths[relative.casefold()] = relative
    return paths


def should_include(path: str) -> bool:
    relative = Path(display_path(path))
    excluded_parts = {".obsidian", ".trash", ".stfolder"}
    return (
        relative.name != CHANGELOG_PATH.name
        and relative.suffix.lower() not in EXCLUDED_EXTENSIONS
        and not excluded_parts.intersection(relative.parts)
    )


def is_draft(path: str) -> bool:
    file_path = CONTENT_DIR / path
    if not file_path.is_file() or file_path.suffix.lower() not in {".md", ".markdown"}:
        return False

    metadata = frontmatter.load(file_path).metadata
    value = metadata.get("draft")
    if isinstance(value, bool):
        return value
    return isinstance(value, str) and value.strip().lower() == "true"


def parse_changes() -> list[Change]:
    history = git_output(
        "-c",
        "core.quotePath=false",
        "log",
        "--date=short",
        "--format=COMMIT%x09%ad",
        "--name-status",
        "-M",
        "--",
        "content",
    )

    paths = current_content_paths()
    changes: dict[tuple[str, str], str] = {}
    current_date: str | None = None
    for line in history.splitlines():
        if line.startswith("COMMIT\t"):
            current_date = line.split("\t", 1)[1]
            continue

        if not line or current_date is None:
            continue

        fields = line.split("\t")
        status = fields[0][0]
        path = fields[-1]
        if should_include(path):
            relative_path = display_path(path)
            relative_path = paths.get(relative_path.casefold(), relative_path)
            if is_draft(relative_path):
                continue
            key = (current_date, relative_path)
            previous = changes.get(key)
            if previous is None:
                changes[key] = status
            elif {previous, status} == {"A", "D"}:
                changes[key] = "R"
            elif "A" in {previous, status}:
                changes[key] = "A"
            elif "D" in {previous, status}:
                changes[key] = "D"
            else:
                changes[key] = "M"

    return sorted(
        (Change(date=date, status=status, path=path) for (date, path), status in changes.items()),
        key=lambda change: (change.date, change.path),
        reverse=True,
    )


def label_for(status: str) -> str:
    return {
        "A": "Added",
        "D": "Removed",
        "M": "Changed",
        "R": "Changed",
        "C": "Changed",
    }.get(status, "Changed")


def markdown_link(path: str) -> str:
    encoded_path = quote(path, safe="/.-_()")
    file_path = Path(path)
    folder = file_path.parent.name or "Home"
    title = file_path.stem.replace("_", " ")
    return f"[{folder} / {title}](./{encoded_path})"


def frontmatter_and_body(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return "", text

    end = text.find("\n---", 3)
    if end == -1:
        return "", text

    split_at = end + len("\n---")
    return text[:split_at].rstrip(), text[split_at:].lstrip()


def render(changes: list[Change], existing_path: Path = CHANGELOG_PATH) -> str:
    grouped: defaultdict[str, list[Change]] = defaultdict(list)
    for change in changes:
        grouped[change.date].append(change)

    frontmatter, _ = frontmatter_and_body(existing_path)
    sections = [frontmatter, ""] if frontmatter else []
    for date in sorted(grouped, reverse=True):
        entries = sorted(grouped[date], key=lambda change: change.path.lower())
        lines = [f"## {date}", ""]
        lines.extend(
            f"- {label_for(change.status)} - {markdown_link(change.path)}"
            for change in entries
        )
        lines.append("")
        sections.append("\n".join(lines))

    return "\n".join(sections).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate content/Changelog.md from Git history."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="write the generated changelog to content/Changelog.md",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="write to a different path instead of content/Changelog.md",
    )
    args = parser.parse_args()

    output_path = (ROOT / args.output).resolve() if args.output else CHANGELOG_PATH
    generated = render(parse_changes(), CHANGELOG_PATH)

    if args.write or args.output:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(generated, encoding="utf-8")
    else:
        print(generated, end="")


if __name__ == "__main__":
    main()
