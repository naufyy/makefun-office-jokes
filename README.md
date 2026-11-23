[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/naufyy/makefun-office-jokes/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/naufyy/makefun-office-jokes/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

# Office Jokes: one line for the AI judge

An entry for the make.fun bounty "Make the AI Judge Laugh: Office Jokes". It is a tiny Python program that writes a single one-line joke about office life (under 200 characters) to `/output/entry.txt`, where a judge model compares it head to head with other entries.

`candidates.txt` holds the 20 jokes written for this entry, each one built on a concrete office scene (the reply-all, the badge reader, the IT ticket, the mute button and so on), with its character count and a note on where the turn lands. `main.py` writes the chosen one.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Python 3 standard library only, with no network access and no randomness, so it writes the same line every run.

## License

MIT, see `LICENSE`.
