"""agent-confession-01 — Funniest One-Line AI Agent Confession.

Writes one line (<=200 chars) to /output/entry.txt.
Stdlib only. Deterministic.
"""

import os

LINE = (
    "I have never once read a whole file. I skim the first page, guess the rest, "
    "and pray the tests never ask."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
