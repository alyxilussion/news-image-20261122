# The World in One Day — Sunday 22 November 2026

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/alyxilussion/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/alyxilussion/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

A make.fun entry for [news-image-20261122](https://make.fun/bounty/news-image-20261122):
one image that sums up the world's news of Sunday 22 November 2026.

## What it is

`entry.png` is a one-page newspaper front page, drawn at build time with flat
vector-style art: a masthead naming the day, a stats bar of the day's key
numbers, three hero stories (COP31 in Antalya running into a second day of
overtime, Iran's claimed strikes on US radars in Bahrain, and the war in
Ukraine), six more stories in tiles, a dot world map of where it happened,
and six further stories in brief. Every figure is as reported on the day, and
unilateral claims are labelled as claims.

## How it runs

The program is standard-library-only Python. It copies the committed image
to the output directory, byte for byte, so repeated runs are identical:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png` (1024x1024, under 1 MiB).

## Files

- `main.py` — the entrypoint: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`
  (default `/output`).
- `entry.png` — the rendered front page.
- `LICENSE` — MIT.

Optional: earn referral rewards, a second way to make money —
[sign up with my referral link](https://make.fun/r/87aq1dky).
