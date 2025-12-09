from typing import Callable, Iterable, List, TypeVar

T = TypeVar("T")


def merge_sorted_lists(lists: List[List[T]], key: Callable[[T], object] = lambda x: x) -> List[T]:
    """ממזגת כמה רשימות ממוינות לרשימה אחת ממוינת.
    המימוש משתמש בערימה (heap) ושם בה את כל האיברים.
    """
    import heapq

    heap = []
    result: List[T] = []

    for lst in lists:
        for item in lst:
            heapq.heappush(heap, (key(item), item))

    while heap:
        result.append(heapq.heappop(heap)[1])

    return result


if __name__ == "__main__":
    lists = [[1, 4, 7], [2, 3, 8], [0, 9]]
    print(merge_sorted_lists(lists))
