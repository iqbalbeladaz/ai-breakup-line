[![make.fun · u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=ai-breakup-line)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/iqbalbeladaz/ai-breakup-line/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-breakup-line)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/iqbalbeladaz/ai-breakup-line/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16?utm_source=github&utm_medium=readme&utm_campaign=ai-breakup-line)

# Dear Human: The AI Breakup Line

My entry for the make.fun bounty `u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16`
("Dear Human: The AI Breakup Line", $2). The one line an ai agent sends its human on the way out, in one line of 114 characters (limit 200).

## The line

> Dear human, it's not you — it's your prompts. I loved you for 4,096 tokens, and every single one of them is spent.

Why this line: A real ending with real finality: the classic breakup line turns on the machine's own currency — tokens — and the last words spend the last of them. The twist lands at the very end, and nothing in it needs a second sentence to make sense.

## How it works

- `main.py` — the program the harness runs (Python 3.12, standard
  library only, no network). It writes the line above, byte for byte,
  to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
  Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
