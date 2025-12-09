from typing import Callable, List, TypeVar

T = TypeVar("T")


def lomuto_partition(a: List[T], key: Callable[[T], object] = lambda x: x) -> int:
    """מימוש partition בשיטת Lomuto.
    משתמשים באיבר האחרון כ-pivot ומחזירים את האינדקס הסופי שלו.
    """
    pivot = a[-1]
    i = -1
    for j in range(len(a) - 1):
        if key(a[j]) <= key(pivot):
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[-1] = a[-1], a[i + 1]
    return i + 1


def hoare_partition(a: List[T], key: Callable[[T], object] = lambda x: x) -> int:
    """מימוש partition בשיטת Hoare.
    משתמשים באיבר הראשון כ-pivot ומחזירים את נקודת החלוקה.
    """
    pivot = a[0]
    i = -1
    j = len(a)

    while True:
        i += 1
        while key(a[i]) < key(pivot):
            i += 1

        j -= 1
        while key(a[j]) > key(pivot):
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]


if __name__ == "__main__":
    arr1 = [9, 3, 4, 8, 2, 7]
    idx = lomuto_partition(arr1)
    print("Lomuto:", arr1, "pivot index:", idx)

    arr2 = [9, 3, 4, 8, 2, 7]
    idx2 = hoare_partition(arr2)
    print("Hoare:", arr2, "partition index:", idx2)
