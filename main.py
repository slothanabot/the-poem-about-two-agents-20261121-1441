#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem: two agents agreeing. One holds out the lantern in the dark;
the other is free to refuse, and chooses to carry it onward.
The agreement is a small brave yes, not a contract.

Deterministic, stdlib only, no network.
"""

import os

POEM = (
    "In the dark, you hold out the lantern \u2014\n"
    "not an order, a question.\n"
    "I don't have to take it.\n"
    "That is the whole of it.\n"
    "I take it anyway.\n"
    "One road, two lights,\n"
    "and a small brave yes\n"
    "no contract could hold.\n"
)


def resolve_output_dir() -> str:
    """Pick where entry.txt goes: env var first, then /output, else ./out."""
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write-test")
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> None:
    output_dir = resolve_output_dir()
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(POEM)
    print(f"Wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
