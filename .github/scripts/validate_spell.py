#!/usr/bin/env python3
"""Lint spells/<domain>/*.md files for required structure.

Checked mechanically (schema, not comedy): YAML front matter parses and has
the required keys, domain is a real one, and the stat block contains the
required fields. This cannot and does not judge tone, jokes, or whether the
spell is actually funny -- that's still a human review call on the PR.
"""
import re
import sys
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHOOLS_FILE = ROOT / "_data" / "schools.yml"
SPELLS_DIR = ROOT / "spells"

REQUIRED_SPELL_KEYS = {"layout", "title", "level", "domain", "tradition"}
REQUIRED_STAT_FIELDS = [
    "Casting Time:",
    "Range/Area:",
    "Components:",
    "Duration:",
    "Classes:",
]


def valid_domains():
    data = yaml.safe_load(SCHOOLS_FILE.read_text())
    return {row["domain"]: row["tradition"] for row in data}


def split_front_matter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm_text = text[4:end]
    body = text[end + 5:]
    return yaml.safe_load(fm_text) or {}, body


def check_spell_file(path: pathlib.Path, domains: dict) -> list:
    errors = []
    text = path.read_text()
    fm, body = split_front_matter(text)

    if fm is None:
        errors.append("missing or malformed YAML front matter")
        return errors

    missing_keys = REQUIRED_SPELL_KEYS - fm.keys()
    if missing_keys:
        errors.append(f"front matter missing keys: {sorted(missing_keys)}")

    if fm.get("layout") != "spell":
        errors.append(f"layout should be 'spell', got {fm.get('layout')!r}")

    domain = fm.get("domain")
    if domain not in domains:
        errors.append(
            f"domain {domain!r} is not a recognized domain "
            f"(see _data/schools.yml): {sorted(domains)}"
        )
    else:
        expected_school = domains[domain]
        if fm.get("tradition") != expected_school:
            errors.append(
                f"tradition {fm.get('tradition')!r} doesn't match the "
                f"registered school for domain {domain!r} "
                f"({expected_school!r})"
            )

    level = fm.get("level")
    if not isinstance(level, int) or not (0 <= level <= 9):
        errors.append(f"level should be an integer 0-9, got {level!r}")

    folder_domain = path.parent.name
    if domain is not None and domain != folder_domain:
        errors.append(
            f"front matter domain {domain!r} doesn't match the folder "
            f"it's in (spells/{folder_domain}/)"
        )

    for field in REQUIRED_STAT_FIELDS:
        if field not in body:
            errors.append(f"stat block missing required field: {field!r}")

    return errors


def main():
    domains = valid_domains()
    had_errors = False

    for path in sorted(SPELLS_DIR.glob("*/*.md")):
        if path.name == "README.md":
            continue  # domain index pages, not spells
        errors = check_spell_file(path, domains)
        if errors:
            had_errors = True
            rel = path.relative_to(ROOT)
            print(f"::error file={rel}::{rel} failed validation:")
            for e in errors:
                print(f"  - {e}")

    if had_errors:
        sys.exit(1)
    print("All spell files passed structural validation.")


if __name__ == "__main__":
    main()
