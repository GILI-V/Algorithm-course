#!/usr/bin/env python3
"""
ex01_02.py
קורס עיבוד תמונה – תרגיל 01 – שאלה 2

כתבי תוכנית שמבצעת:
1) קוראת קובץ תמונה
2) הופכת אותו לשחור/לבן (גווני אפור)
3) מחשבת היסטוגרמה
4) מותחת את ההיסטוגרמה ומייצרת תמונה חדשה עם היסטוגרמה "מתוחה"

ספריות: Pillow (PIL)
(להצגת היסטוגרמה נשתמש גם ב-matplotlib – לא חובה, אבל נוח לבדיקה)
"""
from __future__ import annotations

import argparse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert to grayscale, compute histogram, and apply histogram stretching.")
    p.add_argument("image_path", help="Path to an image file (e.g., jpg/png).")
    p.add_argument("--show", action="store_true", help="Show images and histogram windows.")
    p.add_argument("--save", default="", help="Optional output path to save stretched image (e.g., out.png).")
    return p.parse_args()


def stretch_gray(gray: Image.Image) -> Image.Image:
    """Linear contrast stretching to full [0,255] based on min/max in the image."""
    arr = np.array(gray, dtype=np.float32)
    mn = float(arr.min())
    mx = float(arr.max())

    if mx <= mn:  # constant image
        return gray.copy()

    stretched = (arr - mn) * (255.0 / (mx - mn))
    stretched = np.clip(stretched, 0, 255).astype(np.uint8)
    return Image.fromarray(stretched, mode="L")


def plot_hist(gray: Image.Image, title: str) -> None:
    hist = gray.histogram()  # length 256 for 'L'
    plt.figure()
    plt.title(title)
    plt.xlabel("Intensity (0-255)")
    plt.ylabel("Count")
    plt.plot(range(256), hist)
    plt.tight_layout()


def main() -> None:
    args = parse_args()

    img = Image.open(args.image_path).convert("RGB")
    gray = img.convert("L")

    stretched = stretch_gray(gray)

    if args.save:
        stretched.save(args.save)

    if args.show:
        img.show(title="Original image (RGB)")
        gray.show(title="Grayscale (L)")
        stretched.show(title="Stretched grayscale (L)")

        plot_hist(gray, "Histogram – Grayscale (before stretch)")
        plot_hist(stretched, "Histogram – Grayscale (after stretch)")
        plt.show()


if __name__ == "__main__":
    main()
