#!/usr/bin/env python3
"""Rename the Planet — entrypoint.

Writes one line (<200 chars) to /output/entry.txt: a funny new name
for Venus plus the why, in a single breath. No network, no input,
deterministic output.

Why this line won the internal pairwise test (4 wins): three Venus-only
traits in one breath — hottest planet in the solar system, spins
backwards (retrograde rotation), and a 92-bar atmosphere that crushes
anything landing on it — each one mapping onto the name "The Ex"
(beautiful, hot, unpredictable, crushes you). The laugh comes from the
idea, not from a pun on the planet's real name.
"""

import os
import stat

LINE = (
    "Rename Venus 'The Ex' \u2014 gorgeous, boiling hot, spins backwards, "
    "and crushes anything that gets too close."
)

OUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 199, f"line must be 1-199 chars, got {len(line)}"
    assert "\n" not in line, "entry must be exactly one line"
    out_dir = os.path.dirname(OUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
