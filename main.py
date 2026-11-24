#!/usr/bin/env python3
"""Vending Machine Pickup Line — writes one pickup line to entry.txt.

The machine speaks in the first person and plays a small scheme on the
passing human: its SOLD OUT light is fake, flashed on purpose so the
human comes back tomorrow and presses its buttons again. The punch
("press me again") is the pickup itself, and it lands in the last
three words. Stdlib only, no network, fully deterministic.
"""

import os
import sys

LINE = "My SOLD OUT light is a lie \u2014 I only flash it so you'll come back tomorrow and press me again."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    if "\n" in LINE or "\r" in LINE:
        print("error: line contains a line break", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 200:
        print("error: line length out of range:", len(LINE), file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line has leading or trailing space", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    if (os.stat(path).st_mode & 0o777) != 0o644:
        print("error: file mode is not 0644", file=sys.stderr)
        return 1

    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != LINE:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if back.endswith("\n") or "\n" in back:
        print("error: read-back has a line break", file=sys.stderr)
        return 1
    if not 1 <= len(back) <= 200:
        print("error: read-back length out of range", file=sys.stderr)
        return 1

    print(f"wrote {len(back)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
