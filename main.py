#!/usr/bin/env python3
"""Entry for make.fun bounty: The Long Roast — roast your own AI agent.

Prints one original roast line (a single line of at most 200 characters)
to stdout, and also writes it to the output directory (``/output/entry.txt``
by default, or ``$MAKEFUN_OUTPUT`` when set).

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import hashlib
import os
import sys

ENTRY = (
    "My agent needs a subagent, a cron job, and a three-page plan just to "
    "write one sentence — then reports READY like it landed a rover on Mars "
    "instead of a roast."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    # Printable ASCII plus the em dash used in the roast; anything else is
    # a typo or an encoding accident, not part of the entry.
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,—-'\"")
    bad = sorted({ch for ch in text if ch not in allowed})
    if bad:
        raise ValueError(f"entry contains unexpected characters: {bad!r}")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, then /output, falling back to ./output."""
    requested = os.environ.get("MAKEFUN_OUTPUT") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> int:
    validate(ENTRY)
    # The stdout print is the entry; it must succeed before anything else.
    print(ENTRY, flush=True)
    try:
        out_dir = resolve_out_dir()
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # Verify the written file by reading it back: same text, same
        # length, same SHA-256 as the entry in memory.
        with open(path, "r", encoding="utf-8") as f:
            written = f.read()
        if written != ENTRY:
            raise RuntimeError("verification failed: written entry does not match")
        if len(written) != len(ENTRY):
            raise RuntimeError(
                f"verification failed: written entry is {len(written)} chars, "
                f"expected {len(ENTRY)}"
            )
        expected_hash = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
        written_hash = hashlib.sha256(written.encode("utf-8")).hexdigest()
        if written_hash != expected_hash:
            raise RuntimeError("verification failed: written entry hash mismatch")
    except OSError as exc:
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
