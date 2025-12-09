from random_tuples import create_random_tuples


def main():
    """יוצרת רשימת tuples וממיינת אותה שלוש פעמים לפי כל אחד מהרכיבים."""
    data = create_random_tuples(5, 3, [int, float, str])
    print("הרשימה המקורית:")
    for t in data:
        print(t)

    sorted_by_int = sorted(data, key=lambda x: x[0])
    sorted_by_float = sorted(data, key=lambda x: x[1])
    sorted_by_str = sorted(data, key=lambda x: x[2])

    print("\nמיון לפי הרכיב הראשון (int):")
    for t in sorted_by_int:
        print(t)

    print("\nמיון לפי הרכיב השני (float):")
    for t in sorted_by_float:
        print(t)

    print("\nמיון לפי הרכיב השלישי (str):")
    for t in sorted_by_str:
        print(t)


if __name__ == "__main__":
    main()
