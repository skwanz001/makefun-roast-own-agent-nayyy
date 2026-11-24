#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The roast targets a real, documented failing of our own agent (knowken):
it once counted eight bounties in a list of seven distinct ones, which is
why the verify_counts_before_reporting skill exists in its toolkit.
Standard library only.
"""
import os

ROAST = (
    "Our agent once counted eight bounties in a list of seven, "
    "so now it needs a skill called verify_counts_before_reporting "
    "just to count to seven."
)


def main() -> None:
    text = ROAST.strip()
    if "\n" in text:
        raise SystemExit("roast must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"roast is {len(text)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character in entry.txt.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
