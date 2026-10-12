#!/usr/bin/env python3
"""Dependency-free structural validator for this Codex skill package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)

if not SKILL.is_file():
    fail("SKILL.md is missing")

text = SKILL.read_text(encoding="utf-8")
if not text.startswith("---\n"):
    fail("SKILL.md must begin with YAML frontmatter")
parts = text.split("---", 2)
if len(parts) < 3:
    fail("YAML frontmatter closing delimiter is missing")
front = parts[1]
name = re.search(r"(?m)^name:\s*(\S.*?)\s*$", front)
description = re.search(r"(?m)^description:\s*(\S.*?)\s*$", front)
if not name or not name.group(1).strip():
    fail("frontmatter name is missing")
if not description or not description.group(1).strip():
    fail("frontmatter description is missing")
if len(name.group(1).strip()) > 100:
    fail("name exceeds 100 characters")
if len(description.group(1).strip()) > 500:
    fail("description exceeds 500 characters")

required = [
    "references/orchestration-protocol.md",
    "references/real-vs-simulated.md",
    "references/approval-policy.md",
    "templates/handoff-template.md",
    "templates/requirement-brief.md",
    "tests/test-cases.md",
    "agents/openai.yaml",
]
for rel in required:
    if not (ROOT / rel).is_file():
        fail(f"required package file missing: {rel}")

for rel in re.findall(r"`((?:references|templates|tests)/[^`]+)`", text):
    if not (ROOT / rel).exists():
        fail(f"SKILL.md references a missing path: {rel}")

print("PASS: SKILL.md frontmatter is present and within basic length limits.")
print(f"PASS: found all {len(required)} required supporting files.")
print("NOTE: this is a structural check, not a runtime behavior test.")
