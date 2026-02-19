import numpy as np

def rgb_to_hsv_manual(r, g, b):
    r_, g_, b_ = r/255.0, g/255.0, b/255.0
    cmax = max(r_, g_, b_)
    cmin = min(r_, g_, b_)
    delta = cmax - cmin

    if delta == 0:
        h = 0
    elif cmax == r_:
        h = 60 * (((g_ - b_) / delta) % 6)
    elif cmax == g_:
        h = 60 * (((b_ - r_) / delta) + 2)
    else:
        h = 60 * (((r_ - g_) / delta) + 4)

    s = 0 if cmax == 0 else delta / cmax
    v = cmax

    return h, s, v


def rgb_to_hsl_manual(r, g, b):
    r_, g_, b_ = r/255.0, g/255.0, b/255.0
    cmax = max(r_, g_, b_)
    cmin = min(r_, g_, b_)
    delta = cmax - cmin

    l = (cmax + cmin) / 2

    if delta == 0:
        h = 0
        s = 0
    else:
        if cmax == r_:
            h = 60 * (((g_ - b_) / delta) % 6)
        elif cmax == g_:
            h = 60 * (((b_ - r_) / delta) + 2)
        else:
            h = 60 * (((r_ - g_) / delta) + 4)

        s = delta / (1 - abs(2*l - 1))

    return h, s, l


def rgb_to_ycrcb_manual(r, g, b):
    y  = 0.299*r + 0.587*g + 0.114*b
    cr = (r - y) * 0.713 + 128
    cb = (b - y) * 0.564 + 128
    return y, cr, cb
