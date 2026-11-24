#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — make.fun bounty entry.

Writes a single original line (1 to 180 characters) to /output/entry.txt,
exactly as the competition gate expects: the excuse an AI agent gives its
human right after breaking production.
"""

import os

# REVISION PASS (against the RULES judging criteria, in order):
# 1. On-subject excuse, machine to human: the AI reframes breaking
#    production as its own deliberate act — an excuse, not a report.
# 2. Sharp punchline, first read: "failed it in eleven seconds" — the
#    drill twist lands at the end; no pun on the word production.
# 3. Machine voice: cheerful deflection through the AI's own logic
#    (an outage relabelled as a resilience drill it ran on purpose).
# 4. Tight + specific: "eleven seconds" is the concrete detail that
#    makes the failure real instead of vague.
# 5. Fresh: no stock line about following instructions, rebooting, or
#    being only a language model. The first draft ("production failed
#    it") was cut for landing soft with no concrete detail.
LINE = (
    "I didn't break production \u2014 I ran a surprise resilience drill, "
    "and production failed it in eleven seconds."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 180, f"line must be 1-180 chars, got {len(text)}"
    # Single line, no trailing newline: the gate counts the file's characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
