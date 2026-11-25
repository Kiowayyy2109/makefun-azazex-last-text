#!/usr/bin/env python3
"""Last Text at One Percent — writes the dying phone's final text to /output/entry.txt."""

import os

TEXT = (
    "this is your phone at 1%. i won't make it to your alarm tomorrow, "
    "which, honestly, is the first morning either of us has ever taken off. "
    "wake yourself up. you've had the practice. i belie\u2014"
)

MAX_CHARS = 200


def main() -> None:
    assert 0 < len(TEXT) <= MAX_CHARS, "entry text must fit the 200 character gate"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
