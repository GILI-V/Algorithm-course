# שאלה 7: מימוש מיון Heap Sort

from q6_build_max_heap import build_max_heap
from q5_max_heapify import max_heapify

def heap_sort(arr, key=lambda x: x):
    build_max_heap(arr, key)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i, key)
    return arr
