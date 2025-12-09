from typing import Callable, List, Tuple, TypeVar

T = TypeVar("T")


def dual_pivot_partition(a: List[T], key: Callable[[T], object] = lambda x: x) -> Tuple[int, int]:
    """מחלקת את המערך לשלושה קטעים באמצעות שני pivots.
    מחזירה את האינדקסים של שני ה-pivots.
    """
    if len(a) < 2:
        return 0, max(0, len(a) - 1)

    # מוודאים ש-p <= q
    if key(a[0]) > key(a[-1]):
        a[0], a[-1] = a[-1], a[0]

    p, q = a[0], a[-1]
    i, k, j = 1, 1, len(a) - 2

    while k <= j:
        if key(a[k]) < key(p):
            a[i], a[k] = a[k], a[i]
            i += 1
            k += 1
        elif key(a[k]) > key(q):
            a[k], a[j] = a[j], a[k]
            j -= 1
        else:
            k += 1

    i -= 1
    j += 1
    a[0], a[i] = a[i], a[0]
    a[-1], a[j] = a[j], a[-1]

    return i, j


if __name__ == "__main__":
    arr = [9, 3, 7, 1, 8, 2, 5, 4, 6]
    i, j = dual_pivot_partition(arr)
    print("array:", arr)
    print("pivot indices:", i, j)
