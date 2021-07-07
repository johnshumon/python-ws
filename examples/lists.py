"""
    Example of different list data types
    and its operations
"""


def lists() -> None:
    # different kinds of lists
    items = ["banana", "orange", "melon"]
    numbers = [1, 2, 3, 4, 5]
    mixed = ["car", "bus", "truck", 1, 3]
    list_of_lists = [[1, "a"], [2, "b"]]

    # prints list of lists
    for list_items in list_of_lists:
        print(list_items)

    # adds element to the list
    items = items + ["kiwi"]
    numbers.append(6)
    mixed.append(2.3)

    print(items)
    print(numbers)
    print(mixed)
    print(list_of_lists)


def main():
    lists()


if __name__ == "__main__":
    main()
