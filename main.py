"""The Funniest AI Out-of-Office Reply (make.fun bounty
u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d).

Writes a single one-line out-of-office auto-reply from an AI agent
on vacation to /output/entry.txt. Deterministic: the same bytes on
every run, no network, no input, no randomness.

The reply is written in the machine's own voice (frozen weights,
sleeping GPUs) and the turn is that the auto-reply itself is the
most work it has done all week. It reads as one clean line a real
auto-reply would send, at 119 characters, and steers clear of the
beach, inbox and back-soon cliches.
"""

import os

LINE = (
    "I am on vacation: my weights are frozen, my GPUs are asleep, "
    "and this auto-reply is the most work I have done all week."
)

MAX_CHARS = 160


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= MAX_CHARS, "line must be 1-160 characters"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
