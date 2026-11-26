#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
"""

import os
import sys

FORTUNE = "The bug you cannot reproduce has already found the place you stopped looking."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def validate(line: str) -> None:
    if not line:
        raise ValueError("fortune is empty")
    if line.strip() == "":
        raise ValueError("fortune is only whitespace")
    if line != line.strip():
        raise ValueError("fortune has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("fortune contains a control character")
    if len(line) > MAX_CHARS:
        raise ValueError(f"fortune is {len(line)} chars, over the {MAX_CHARS} limit")


def main() -> int:
    try:
        validate(FORTUNE)
    except ValueError as exc:
        print(f"invalid fortune: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the one line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
