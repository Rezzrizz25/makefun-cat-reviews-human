#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human - make.fun entry.

Writes one funny single-line one-star review, written by a house cat
about its human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), the one text the house judge compares two at a
time. Python 3.13, standard library only, no network, reads nothing
from outside the repository. Deterministic: the same line every run.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
    cat out/entry.txt
"""

import os
import sys
from pathlib import Path

ENTRY = "One star. She locks the bedroom door at night like she owns the house. I own the house. I screamed for forty minutes until she opened it, then walked away."
# The joke: the cat demands the closed door be opened, then walks away
# the moment it is - the complaint is the closed door (a recognisable
# cat grievance), the voice is pure cat (the house is mine, the human
# is staff), and the sting lands on the last three words. "For forty
# minutes" makes the screaming concrete: this cat committed to the
# bit. Final line: 155 characters, one line, deadpan review shape.


def main() -> int:
    # Guard: the entry must be non-blank, a single line, and 1-200
    # characters (the bounty caps the line at 200). Fail loudly
    # instead of writing a bad entry - a bad file would score 0.
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > 200:
        print(
            f"entry is {len(ENTRY)} characters, over the 200-character limit",
            file=sys.stderr,
        )
        return 1
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {out / 'entry.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
