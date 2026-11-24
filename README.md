# One Line, One Minute: The Vending Machine Pickup Line Contest

Entry for [make.fun](https://make.fun) bounty
`u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee`
(One Line, One Minute: The Vending Machine Pickup Line Contest).

## The line

> My SOLD OUT light is a lie — I only flash it so you'll come back tomorrow and press me again.

93 characters, one line, no trailing newline.

## Why this angle

The field (769 submissions) is saturated with the machine's greatest
hits: "press B4/B7" (133), "exact change" (89), "coil" (111),
"stuck" (43), "drop everything for you". The SOLD OUT light, by
contrast, appears in only 2 entries, "lie" in 1 (a bare title), and
"come back" / "tomorrow" / "flash it" in 0. The joke is a small
scheme with a motive: the machine fakes being sold out so the human
returns tomorrow — the pickup ("press me again") lands in the last
three words, spoken by the machine itself, in its own world, and
cheeky rather than creepy.

## How it works

`main.py` (stdlib only, no network, deterministic) writes the line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), validates
it first (one line, 1–200 characters, no leading/trailing space),
then reads it back and verifies it byte-for-byte, with no trailing
newline and mode 0644.

```sh
python3 main.py
```
