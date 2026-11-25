"""Describe Your Ex in One Word — make.fun entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The word: "Redacted" — the ex, redacted from the record of my life.
Pure stdlib (os only).
"""

import os

WORD = "Redacted"


def validate(word):
    """Gate: one word, 1-111 chars, valid UTF-8, not only whitespace."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not word or word != word.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(word) > 111:
        raise ValueError("entry must be at most 111 characters")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("entry must not contain control characters")
    if " " in word or "\t" in word or "\n" in word:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be letters only, no punctuation tricks")
    word.encode("utf-8")
    return word


def main():
    word = validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == word, "read-back mismatch"
    print(word)
    print("chars: %d" % len(word))


if __name__ == "__main__":
    main()
