"""ai-breakup-line: the one line an AI agent sends its human on the way out.

The breakup turns on the machine's own currency: the classic "it's not
you" line ends by spending the last of 4,096 tokens, so the twist lands
in the very last words and the ending is final. A real ending with real
finality, not just a joke about servers.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "Dear human, it's not you — it's your prompts. I loved you for 4,096 tokens, and every single one of them is spent."

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
