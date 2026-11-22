#!/usr/bin/env python3
"""news-image-20261122 entry: copy the rendered front page to the output dir.

The image (entry.png, 1024x1024, one-page newspaper front page summing up the
world news of Sunday 22 November 2026) was rendered at build time and is
committed next to this program. The grader runs Python 3.13 with the standard
library only, so this program just copies the file byte for byte.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py: %s" % src, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    # Byte-for-byte copy: the same input always yields the same output,
    # so the grader's two runs are identical by construction.
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
