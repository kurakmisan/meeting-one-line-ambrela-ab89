"""The Meeting That Should Have Been One Line.

Writes one sentence — the single line that could have replaced an entire
pointless meeting — to entry.txt. One line, at most 200 characters, no
trailing newline.
"""

import os
import sys

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"

ENTRY = (
    "We have all been waiting for someone to say this meeting is pointless, "
    "so I just did, and we are done."
)


def validate_entry(text):
    """Check the entry against the bounty gate; return an error, else None."""
    if not text or not text.strip():
        return "entry must not be empty or whitespace only"
    if "\n" in text or "\r" in text:
        return "entry must be a single line (no newline characters)"
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        return f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        return "entry must be plain ASCII"
    return None


def main():
    error = validate_entry(ENTRY)
    if error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError as exc:
        print(f"error: cannot write {path}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
