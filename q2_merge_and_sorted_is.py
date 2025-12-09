from typing import Callable, Iterable, List, TypeVar, Optional

T = TypeVar("T")


def sorted_is(a: List[T], key: Callable[[T], object] = lambda x: x) -> bool:
    """בודקת אם הרשימה a מסודרת בסדר לא יורד לפי key."""
    return all(key(a[i]) <= key(a[i + 1]) for i in range(len(a) - 1))


def merge(a: List[T], b: List[T], key: Callable[[T], object] = lambda x: x) -> Optional[List[T]]:
    """ממזגת שתי רשימות ממוינות a ו-b לרשימה ממוינת חדשה.
    אם אחת הרשימות לא ממוינת – מחזירה None.
    """
    if not sorted_is(a, key) or not sorted_is(b, key):
        return None

    i = j = 0
    result: List[T] = []

    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # מוסיפים את השאריות
    result.extend(a[i:])
    result.extend(b[j:])
    return result


if __name__ == "__main__":
    # דוגמה קצרה להרצה
    a = [1, 3, 5]
    b = [2, 4, 6]
    print(merge(a, b))
