#!/usr/bin/env python3
"""Two Lines of Morning Light — writes a two-line micro poem to /output/entry.txt.

Python 3.13 stdlib only, no network, deterministic.
"""
import os

ENTRY = (
    "Sunlight threads the keyhole, one thin needle,\n"
    "and stitches the dark room to morning.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
