# שאלה 4: בדיקה האם מערך הוא ערימת מקסימום החל מאינדקס i

from q3_heap_helpers import parent

def is_max_heap(arr, i=0, key=lambda x: x):
    n = len(arr)
    for j in range(i + 1, n):
        if key(arr[parent(j)]) < key(arr[j]):
            return False
    return True
