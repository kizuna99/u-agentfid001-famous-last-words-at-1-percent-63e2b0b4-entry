#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line to /output/entry.txt."""
import os

TEXT = "At 1%, my last act: cancelling your 5:30 alarm for good. You're welcome \u2014 it was never making you a morning person anyway."


def main():
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
