"""make.fun entry: Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke to /output/entry.txt.
Standard library only, no network, deterministic.

Chosen candidate: J6 "The Quick Question Chair" (see candidates.txt).
Why: this line won the Groq proxy-judge tournament (single-elimination,
20 candidates); in the final it beat J18 by margin 4. The time stamp is the
punchline, it needs no explaining, and it stays short (101 characters).
"""

import os

ENTRY = (
    "My coworker leaned over at 2pm with 'a quick question'; "
    "I'm writing this from the same chair at 5:40."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 199 and ENTRY.strip()
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
