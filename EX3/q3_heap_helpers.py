# שאלה 3: פונקציות עזר לערימה (parent, left, right)

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2
