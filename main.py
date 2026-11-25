"""The Meeting That Should Have Been One Line.

Writes one sentence — the single line that could have replaced an entire
pointless meeting — to entry.txt. One line, at most 200 characters, no
trailing newline.
"""

import os

ENTRY = (
    "We have all been waiting for someone to say this meeting is pointless, "
    "so I just did, and we are done."
)


def main():
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    ENTRY.encode("ascii")  # entry must be plain ASCII
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
