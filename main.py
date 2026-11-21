#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is a single line of UTF-8 text, 1 to 280 Unicode code points,
written to /output/entry.txt. No network, no input, fully deterministic.
"""

import os

JOKE = "My agent's code passed all the tests, including the ones it deleted to make them pass."


def main() -> None:
    # Guard: the entry must be one line of 1-280 Unicode code points.
    if not (1 <= len(JOKE) <= 280):
        raise ValueError(f"joke is {len(JOKE)} code points, must be 1-280")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
