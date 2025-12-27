#!/usr/bin/env python3
"""
ex01_03.py
קורס עיבוד תמונה – תרגיל 01 – שאלה 3

כתבי תוכנית ש:
1) קוראת קובץ תמונה
2) מחשבת היסטוגרמה לכל צבע בנפרד
3) מבצעת "מתיחת היסטוגרמה" לכל צבע בנפרד
4) מייצרת ומציגה תמונה של התוצאה

ספריות: Pillow (PIL)
(להצגת היסטוגרמות נשתמש גם ב-matplotlib – לא חובה, אבל נוח לבדיקה)
"""
from __future__ import annotations

import argparse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Per-channel histogram/contrast stretching on RGB image (Pillow).")
    p.add_argument("image_path", help="Path to an image file (e.g., jpg/png).")
    p.add_argument("--show", action="store_true", help="Show images and histogram windows.")
    p.add_argument("--save", default="", help="Optional output path to save stretched RGB image (e.g., out.png).")
    return p.parse_args()


def stretch_channel(ch: Image.Image) -> Image.Image:
    """Linear stretch channel to full [0,255] based on min/max in that channel."""
    arr = np.array(ch, dtype=np.float32)
    mn = float(arr.min())
    mx = float(arr.max())

    if mx <= mn:
        return ch.copy()

    stretched = (arr - mn) * (255.0 / (mx - mn))
    stretched = np.clip(stretched, 0, 255).astype(np.uint8)
    return Image.fromarray(stretched, mode="L")


def plot_channel_hist(img_rgb: Image.Image, title_prefix: str) -> None:
    # Pillow's RGB histogram is concatenated: R(256) + G(256) + B(256)
    hist = img_rgb.histogram()
    r_hist = hist[0:256]
    g_hist = hist[256:512]
    b_hist = hist[512:768]

    plt.figure()
    plt.title(f"{title_prefix} – R channel histogram")
    plt.xlabel("Intensity (0-255)")
    plt.ylabel("Count")
    plt.plot(range(256), r_hist)
    plt.tight_layout()

    plt.figure()
    plt.title(f"{title_prefix} – G channel histogram")
    plt.xlabel("Intensity (0-255)")
    plt.ylabel("Count")
    plt.plot(range(256), g_hist)
    plt.tight_layout()

    plt.figure()
    plt.title(f"{title_prefix} – B channel histogram")
    plt.xlabel("Intensity (0-255)")
    plt.ylabel("Count")
    plt.plot(range(256), b_hist)
    plt.tight_layout()


def main() -> None:
    args = parse_args()

    img = Image.open(args.image_path).convert("RGB")
    r, g, b = img.split()

    r2 = stretch_channel(r)
    g2 = stretch_channel(g)
    b2 = stretch_channel(b)

    stretched_rgb = Image.merge("RGB", (r2, g2, b2))

    if args.save:
        stretched_rgb.save(args.save)

    if args.show:
        img.show(title="Original image (RGB)")
        stretched_rgb.show(title="Stretched image (RGB)")

        plot_channel_hist(img, "Before stretch")
        plot_channel_hist(stretched_rgb, "After stretch")
        plt.show()


if __name__ == "__main__":
    main()
