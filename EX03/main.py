import sys
import cv2
import numpy as np
from color_models import *

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py R G B")
        return

    r = int(sys.argv[1])
    g = int(sys.argv[2])
    b = int(sys.argv[3])

    print("\nManual Calculations")
    hsv_m = rgb_to_hsv_manual(r, g, b)
    hsl_m = rgb_to_hsl_manual(r, g, b)
    ycrcb_m = rgb_to_ycrcb_manual(r, g, b)

    print("HSV:", hsv_m)
    print("HSL:", hsl_m)
    print("YCrCb:", ycrcb_m)

    rgb = np.uint8([[[r, g, b]]])

    print("\nOpenCV Calculations")

    hsv_cv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    hls_cv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HLS)
    ycrcb_cv = cv2.cvtColor(rgb, cv2.COLOR_RGB2YCrCb)

    print("HSV:", hsv_cv[0][0])
    print("HSL (OpenCV calls it HLS):", hls_cv[0][0])
    print("YCrCb:", ycrcb_cv[0][0])

if __name__ == "__main__":
    main()
