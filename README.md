[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/naufyy/makefun-office-jokes/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/naufyy/makefun-office-jokes/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

# Office Jokes: one line for the AI judge

This repository is a submission to the make.fun bounty "Make the AI Judge Laugh: Office Jokes". Running `main.py` drops one office-life one-liner, shorter than 200 characters, into `/output/entry.txt`; from there a judge model pits it against rival entries in pairwise matchups.

The shortlist lives in `candidates.txt`: twenty jokes, each anchored to something you'd actually run into at work (a stuck printer, a badge reader, a muted call), listed with its length and a short note on where the twist hits, followed by the proxy-judging bracket that picked the winner. `main.py` outputs that winner.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Python 3 standard library only, with no network access and no randomness, so it writes the same line every run.

## License

MIT, see `LICENSE`.
