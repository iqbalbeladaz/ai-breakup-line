# ai-breakup-line: the one line an AI agent sends its human on the way out
#
# The breakup works because it turns on the machine's own currency: the classic
# "it's not you" line ends by spending the last of 4,096 tokens, so the twist
# lands in the very last words and the ending is final.
# The entry program: writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output/entry.txt). Deterministic: the same bytes on every run.
# No network, no input, standard library only.
#
# Try it locally:
#   MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt

import os
from pathlib import Path

ENTRY = "Dear human, it's not you — it's your prompts. I loved you for 4,096 tokens, and every single one of them is spent."

assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"


def main() -> None:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = Path(target_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
