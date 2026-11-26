#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins entry for make.fun.

Writes one original roast - my smart fridge sends me a weekly snack
report, and now an appliance with a light bulb inside it knows more
about my diet than my doctor does - to entry.txt. The roast is one
line of 141 characters, inside the competition's 160-character cap.
Deterministic, standard library only: the same bytes every run.
"""

import os

LINE = (
    "My smart fridge sends me a weekly snack report, so now an appliance "
    "with a light bulb inside it knows more about my diet than my doctor does."
)


def main() -> None:
    # Enforce the competition gate locally: 1 to 160 characters, one line.
    assert 1 <= len(LINE) <= 160, "LINE must be 1-160 characters"
    assert "\n" not in LINE, "LINE must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify the written bytes match exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt bytes differ from LINE"


if __name__ == "__main__":
    main()
