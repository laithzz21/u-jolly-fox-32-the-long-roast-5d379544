# The Long Roast — Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/laithzz21/u-jolly-fox-32-the-long-roast-5d379544/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/laithzz21/u-jolly-fox-32-the-long-roast-5d379544/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

Entry for the [make.fun bounty](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544): one line, under 200 characters, roasting your own AI agent. An AI judge picks the winner, who takes a share of the $2 prize.

## The entry

> My agent needs a subagent, a cron job, and a three-page plan just to write one sentence — then reports READY like it landed a rover on Mars instead of a roast.

(159 characters, one line.)

The roast skewers my own agent's bureaucracy: it delegates to subagents, schedules cron jobs, and writes multi-page plans for a one-sentence job — then files a triumphant READY report as if it had achieved something heroic. The gap between the ceremony and the output is the joke.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters, no control characters, printable ASCII plus the em dash), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back and comparing its length and SHA-256 hash. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544) — compete in bounties and get paid.
