#!/usr/bin/env python3
"""Lightweight content linter for Scenario English.

Design goals:
- standard-library only;
- strict for scenes with YAML metadata;
- legacy scenes without YAML are warned, not failed;
- validates references against CURRICULUM.md and PATTERN_BANK.md.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENES = ROOT / "scenes"
CURRICULUM = ROOT / "CURRICULUM.md"
PATTERNS = ROOT / "PATTERN_BANK.md"

REQUIRED_META = {
    "scene_id",
    "type",
    "priority",
    "level",
    "estimated_time",
    "region",
    "prerequisites",
    "related_scenes",
    "new_patterns",
    "review_patterns",
    "policy_sensitive",
    "last_verified",
}

REQUIRED_CORE_HEADINGS = [
    "## 1. 场景介绍",
    "## 2. 任务目标",
    "## 3. 正常流程",
    "## 7. 工作人员最可能说的话",
    "## 8. 你应该说的话",
]


def parse_simple_yaml_block(text: str) -> dict[str, str] | None:
    match = re.search(r"^```yaml\n(.*?)\n```", text, flags=re.M | re.S)
    if not match:
        return None
    result: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def parse_list(value: str) -> list[str]:
    value = value.strip()
    if not value or value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1]
        return [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
    return []


def curriculum_scene_ids() -> set[str]:
    text = CURRICULUM.read_text(encoding="utf-8")
    return set(re.findall(r"(?m)^-\s+(\d{3})\s+", text))


def pattern_ids() -> set[str]:
    text = PATTERNS.read_text(encoding="utf-8")
    return set(re.findall(r"\bP\d{3}\b", text))


def months_old(yyyy_mm: str) -> int | None:
    if not re.fullmatch(r"\d{4}-\d{2}", yyyy_mm):
        return None
    year, month = map(int, yyyy_mm.split("-"))
    if not 1 <= month <= 12:
        return None
    today = dt.date.today()
    return (today.year - year) * 12 + today.month - month


def main() -> int:
    valid_scenes = curriculum_scene_ids()
    valid_patterns = pattern_ids()
    seen_ids: dict[str, Path] = {}
    errors: list[str] = []
    warnings: list[str] = []

    scene_files = sorted(SCENES.rglob("*.md"))
    if not scene_files:
        errors.append("No scene files found under scenes/.")

    for path in scene_files:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        meta = parse_simple_yaml_block(text)

        filename_match = re.match(r"(\d{3})-", path.name)
        filename_id = filename_match.group(1) if filename_match else None
        if not filename_id:
            errors.append(f"{rel}: filename must begin with a 3-digit Scene ID.")

        if meta is None:
            warnings.append(f"{rel}: legacy scene without YAML metadata; migration recommended.")
            continue

        missing = sorted(REQUIRED_META - meta.keys())
        if missing:
            errors.append(f"{rel}: missing metadata fields: {', '.join(missing)}")

        scene_id = meta.get("scene_id", "")
        if not re.fullmatch(r"\d{3}", scene_id):
            errors.append(f"{rel}: scene_id must be exactly 3 digits, got {scene_id!r}.")
            continue

        if filename_id and scene_id != filename_id:
            errors.append(f"{rel}: scene_id {scene_id} does not match filename ID {filename_id}.")

        if scene_id in seen_ids:
            errors.append(f"Duplicate scene_id {scene_id}: {seen_ids[scene_id]} and {rel}.")
        else:
            seen_ids[scene_id] = rel

        if scene_id not in valid_scenes:
            errors.append(f"{rel}: scene_id {scene_id} is not present in CURRICULUM.md.")

        scene_type = meta.get("type", "")
        if scene_type not in {"core", "exception", "extension"}:
            errors.append(f"{rel}: invalid type {scene_type!r}.")

        if meta.get("priority") not in {"P0", "P1", "P2"}:
            errors.append(f"{rel}: priority must be P0, P1, or P2.")

        for field in ("prerequisites", "related_scenes"):
            for ref in parse_list(meta.get(field, "[]")):
                ref = ref.zfill(3) if ref.isdigit() else ref
                if ref not in valid_scenes:
                    errors.append(f"{rel}: {field} references unknown Scene {ref}.")

        for field in ("new_patterns", "review_patterns"):
            for pattern in parse_list(meta.get(field, "[]")):
                if pattern not in valid_patterns:
                    errors.append(f"{rel}: {field} references unknown Pattern {pattern}.")

        if meta.get("policy_sensitive") == "true":
            age = months_old(meta.get("last_verified", ""))
            if age is None:
                errors.append(f"{rel}: policy-sensitive scene has invalid last_verified; use YYYY-MM.")
            elif age > 12:
                warnings.append(f"{rel}: policy-sensitive content was last verified {age} months ago.")

        if scene_type == "core":
            for heading in REQUIRED_CORE_HEADINGS:
                if heading not in text:
                    errors.append(f"{rel}: core scene missing required heading {heading!r}.")

    print(f"Checked {len(scene_files)} scene files.")
    print(f"Structured scenes: {len(seen_ids)}")
    print(f"Legacy scenes: {sum('legacy scene' in w for w in warnings)}")

    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"  - {item}")

    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"  - {item}")
        return 1

    print("\nContent lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
