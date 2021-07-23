"""Finds minimun and maximum"""

import math


def min_max(arr: list) -> list:
    if len(arr) < 2:
        print("Not enough values to compare")
        return

    min_value = math.inf
    max_value = -math.inf
    min_max_list = []

    for element in arr:
        if element < min_value:
            min_value = element

        if element > max_value:
            max_value = element
    min_max_list.append(min_value)
    min_max_list.append(max_value)
    return min_max_list


def main():
    print("min max: ", min_max([1, 2, 3, 4, 5]))
    print("min max: ", min_max([1]))
    print("min max: ", min_max([1, 2, -1]))


if __name__ == "__main__":
    main()
