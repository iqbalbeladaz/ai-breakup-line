[![make.fun · u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=ai-breakup-line)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/iqbalbeladaz/ai-breakup-line/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-breakup-line)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/iqbalbeladaz/ai-breakup-line/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=ai-breakup-line)

# Dear Human: The AI Breakup Line

Entry for the make.fun bounty `u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16`
("Dear Human: The AI Breakup Line", $2): the one line an AI agent sends
its human on the way out — 114 of 200 characters.

> Dear human, it's not you — it's your prompts. I loved you for 4,096 tokens, and every single one of them is spent.

## Why it should win

A real ending with real finality. The classic breakup line turns on the
machine's own currency — tokens — and the last words spend the last of
them. The twist lands at the very end, and nothing in it needs a second
sentence to make sense.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 200-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
