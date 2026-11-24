"""Seventeen Syllables of Debugging — make.fun bounty entry.

Writes a single haiku about debugging to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure Python standard library, deterministic: the same
bytes on every run.
"""

import os
import re

HAIKU = "\n".join(
    [
        "Three a.m. cursor",
        "blinks at a log line lying",
        "the bug was my own",
    ]
)

EXPECTED_SYLLABLES = (5, 7, 5)
MAX_CHARS = 200

# Small built-in syllable counter: counts vowel groups, with a few
# adjustments for silent trailing "e" and common endings.
_VOWEL_RUN = re.compile(r"[aeiouy]+", re.IGNORECASE)


def count_syllables(word):
    """Best-effort syllable count for a single English word."""
    w = word.strip().lower().strip(".,;:!?\"'()[]")
    if not w:
        return 0
    # "a.m." is spoken as two syllables: "ay em". Check before punctuation
    # stripping eats the trailing dot.
    if word.strip().lower().rstrip(".") in ("a.m",):
        return 2
    if w in ("a", "i"):
        return 1
    groups = _VOWEL_RUN.findall(w)
    count = len(groups)
    # "y" + vowel after a consonant is two syllables, not one run:
    # "lying" = ly-ing, "trying" = try-ing, "dying" = dy-ing.
    if re.search(r"[bcdfghjklmnpqrstvwxz]yi", w):
        count += 1
    # Silent trailing "e" (e.g. "line", "blinks" has none, "the" handled below).
    if w.endswith("e") and count > 1 and not w.endswith("le"):
        count -= 1
    # "-ing" words where the vowel before "ing" is silent-ish are already
    # counted correctly by the vowel-group rule ("lying" -> y + i = 2).
    return max(count, 1)


def validate(text):
    """Enforce the competition gate; raise ValueError on any violation."""
    if text != HAIKU:
        raise ValueError("text is not the exact haiku")
    if text.endswith("\n"):
        raise ValueError("haiku must not end with a trailing newline")
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError("haiku must have exactly 3 lines, got %d" % len(lines))
    for line in lines:
        if not line.strip():
            raise ValueError("haiku lines must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("haiku exceeds %d characters" % MAX_CHARS)
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        words = line.split()
        total = sum(count_syllables(w) for w in words)
        if total != expected:
            raise ValueError(
                "line %r has %d syllables, expected %d" % (line, total, expected)
            )
    return True


def main():
    validate(HAIKU)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = HAIKU.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back what landed on disk and re-validate the exact bytes.
    with open(path, "rb") as f:
        landed = f.read()
    if landed != data:
        raise ValueError("entry.txt on disk does not match the haiku bytes")
    if len(landed) != 63:
        raise ValueError("entry.txt must be exactly 63 bytes, got %d" % len(landed))
    if landed.endswith(b"\n"):
        raise ValueError("entry.txt must not end with a trailing newline")
    validate(landed.decode("utf-8"))
    print("wrote %s (%d bytes)" % (path, len(landed)))


if __name__ == "__main__":
    main()
