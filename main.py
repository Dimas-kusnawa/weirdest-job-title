#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title to /output/entry.txt.
"""
import os

# The title is a real-sounding corporate role with one absurd twist:
# a senior writer whose entire job is apologizing to the office printer,
# the machine everyone hates and nobody can fix. 44 characters, well
# inside the 60-character cap, and nothing else in the output.
TITLE = "Senior Apology Writer for the Office Printer"


# Deterministic: the same title every run, no randomness, no network.
# Output is a single line with no trailing newline, UTF-8, 1-60 chars.
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)
    print(f"wrote {path}: {TITLE} ({len(TITLE)} chars)")


if __name__ == "__main__":
    main()
