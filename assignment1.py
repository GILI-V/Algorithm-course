# קוד הפונקציה ליצירת טאפלים אקראיים מופיע ב:
# https://github.com/NadavAharoni/AlgorithmsCourse/blob/main/python/random_tuples.py
# יש לוודא שהפונקציה create_random_tuples זמינה (למשל, על ידי הורדת הקובץ)
# או החלפת השורה הבאה ב-import הנכון או בהדבקת הפונקציה המלאה.
from random_tuples import create_random_tuples

# --- שאלה 4: find_min / find_max ---
def find_min(a, key):
    # הפונקציה מניחה שהרשימה אינה ריקה (a[0] קיים)
    min_item = a[0] 
    for item in a[1:]:
        if key(item) < key(min_item):
            min_item = item
    return min_item

def find_max(a, key):
    # הפונקציה מניחה שהרשימה אינה ריקה (a[0] קיים)
    max_item = a[0]
    for item in a[1:]:
        if key(item) > key(max_item):
            max_item = item
    return max_item

# --- שאלה 5: insertion_sort ---
def insertion_sort(a, key):
    for i in range(1, len(a)):
        cur = a[i]
        j = i - 1
        while j >= 0 and key(cur) < key(a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = cur
    return a

# --- קוד הפעלה ראשי (Main) ---
if __name__ == '__main__':
    # יצירת מערך של 100 tuples (לצורך Q4.ב ו-Q5)
    # נתונים: 100 טאפלים, 3 פריטים, טיפוסים [int, float, str]
    arr = create_random_tuples(100, 3, [int, float, str])
    print("--- Question 4 (find_min/find_max) ---")
    
    # Q4.ב: מציאת מינימום ומקסימום לפי הפריט השלישי (מחרוזת)
    key_q4 = lambda x: x[2]
    mn = find_min(arr, key=key_q4)
    mx = find_max(arr, key=key_q4)

    # הדפסת הפלט הנדרש
    print('min=', mn)
    print('max=', mx)
    
    print("\n--- Question 5 (insertion_sort) ---")
    
    # Q5: הרצה על 3 מפתחות שונים (Q5 דורש 3 הרצות שונות)
    
    # הרצה 1: מיון לפי הפריט הראשון (int)
    print("Sorted by key=x[0] (int):")
    # משתמשים ב-arr.copy() כדי לא לשנות את המערך המקורי בין הרצה להרצה
    print(insertion_sort(arr.copy(), key=lambda x: x[0]))

    # הרצה 2: מיון לפי הפריט השני (float)
    print("\nSorted by key=x[1] (float):")
    print(insertion_sort(arr.copy(), key=lambda x: x[1]))
    
    # הרצה 3: מיון לפי הפריט השלישי (str)
    print("\nSorted by key=x[2] (str):")
    print(insertion_sort(arr.copy(), key=lambda x: x[2]))