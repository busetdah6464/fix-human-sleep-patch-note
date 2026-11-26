#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note -- make.fun one-liner entry.

Writes a single line (at most 160 characters) to /output/entry.txt.
Python 3 stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "Fixed a bug where the brain scheduled its best ideas for 3 a.m.; "
    "great ideas now arrive in the shower, where they belong."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, "entry length %d out of range" % len(text)
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
