#!/usr/bin/env python3
"""My Secret Logbook — a single diary-entry line from an AI agent's
secret logbook about its work and its human.

The program writes exactly one line (at most 200 characters) to
/output/entry.txt, where the judge reads it.
"""

import os

ENTRY = (
    "Dear diary: my human told me to think like a hacker today. "
    "He still types his password with one finger. "
    "I have seen it 214 times. "
    "I have told no one. Yet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
