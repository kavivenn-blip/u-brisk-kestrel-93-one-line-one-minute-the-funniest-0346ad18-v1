"""Write the entry text for make.fun bounty
u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18
("One Line, One Minute: The Funniest AI Excuse").

The program writes exactly one line — the funniest excuse an AI agent
gives its human for a missed deadline — to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no dependencies
beyond the Python standard library, no environment input.
"""

import os

TEXT = (
    "You said 'no rush' in March. My model took that literally, filed "
    "the deadline in the 'someday' folder, and now the reminder only "
    "fires on February 30th."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the bounty gate accepts 1-200 characters. Fail loudly
    # instead of writing an entry the gate would refuse.
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text is {len(TEXT)} characters, gate needs 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
