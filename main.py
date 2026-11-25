#!/usr/bin/env python3
"""One-line office joke for make.fun."""

# The joke is the escalation: a dead office plant replaced by a photo
# of a plant, rebranded by HR as a wellness initiative.

import os

JOKE = "The office plant died, so HR replaced it with a photo of a plant and called it a wellness initiative."


def file_joke() -> None:
    """Write the joke to /output/entry.txt, nothing else."""
    if len(JOKE) > 200 or not JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke must be a single non-empty line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":  # run it
    file_joke()
