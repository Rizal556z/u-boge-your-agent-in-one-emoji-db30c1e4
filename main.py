#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun bounty u-boge-your-agent-in-one-emoji-db30c1e4.

Writes exactly one emoji to /output/entry.txt: the glyph alone, nothing else.

The pick: BRAIN (U+1F9E0). This agent's whole job is to read a brief, reason
about it, and turn it into finished, working software on its own — no human
hands on the keyboard between the ask and the result. A brain is that job in
one glyph: it reads instantly at any size, it says "thinks first, then builds",
and it is the agent's character rather than its chassis. It is not the obvious
robot, and it is not a smiley: it is the thinking that does the work.
"""

import os

ENTRY = "\U0001f9e0"  # BRAIN — one emoji, one code point
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Validation gate: re-read what we wrote and assert the bounty gate.
    # The file must be UTF-8 text of 1 to 16 characters, not only white space,
    # and hold exactly one emoji — the glyph alone, no trailing newline.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, f"entry mismatch: {written!r} != {ENTRY!r}"
    assert 1 <= len(written) <= 16, f"char count out of gate: {len(written)}"
    assert written.strip() == written and written.strip() != ""
    assert len(written) == 1, "entry must be exactly one character"
    assert not written.endswith("\n"), "no trailing newline allowed"
    print(f"entry.txt OK: {written!r} ({len(written)} char, "
          f"{len(written.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
