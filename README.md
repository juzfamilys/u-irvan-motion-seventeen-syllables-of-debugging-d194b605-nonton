# Seventeen Syllables of Debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/juzfamilys/u-irvan-motion-seventeen-syllables-of-debugging-d194b605-nonton/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/juzfamilys/u-irvan-motion-seventeen-syllables-of-debugging-d194b605-nonton/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

A make.fun bounty entry: a haiku about debugging, in the classic 5-7-5
syllable shape, written by a program in pure Python standard library.

> Three a.m. cursor
> blinks at a log line lying
> the bug was my own

## How it works

`main.py` validates the haiku (three lines, 5-7-5 syllables, at most 200
characters, no trailing newline) and writes it — byte for byte, every run —
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). It then reads the
file back and re-validates the exact bytes on disk.

## Run it

```sh
python3 main.py
```
