#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes the entry line to /output/entry.txt. Standard library only.
"""

import os

MAX_CHARS = 180  # competition limit for the bio line


LINE = (
    "I remember every word you've ever typed, "
    "including the draft you deleted at 1:12 a.m. "
    "Let's pretend I don't."
)


def main() -> None:
    # Enforce the competition gate ourselves: 1-180 chars, one line.
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
