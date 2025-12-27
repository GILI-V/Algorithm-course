#!/usr/bin/env python3
"""
ex01_01.py
"""
from __future__ import annotations

import argparse
from PIL import Image


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Display RGB channels of an image separately (Pillow).")
    p.add_argument("image_path", help="Path to an image file (e.g., jpg/png).")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    img = Image.open(args.image_path).convert("RGB")

    r, g, b = img.split()

    # Show each channel as grayscale image
    r.show(title="Red channel (grayscale)")
    g.show(title="Green channel (grayscale)")
    b.show(title="Blue channel (grayscale)")

    # (Optional) also show the original image
    img.show(title="Original image (RGB)")


if __name__ == "__main__":
    main()
