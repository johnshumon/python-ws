"""Tuple module
This module contains some basic
example of tuples
"""

from typing import Any


def str_to_tuple(passed_str: str) -> None:
    result = tuple(map(int, passed_str.split(", ")))
    print("Tuple after conversion: {}".format(result))


def convert_to_tuple(passed_val: Any) -> tuple:
    converted_val = str(passed_val)
    result = tuple(converted_val)

    print("Tuple after conversion: {}".format(result))
    return result


def iterate_tuple(passed_val: Any) -> None:
    items = convert_to_tuple(passed_val)

    for item in items:
        print(item)


def main():
    # str_to_tuple("7, 8, 0, 3, 45, 3, 2, 22, 4")
    # convert_to_tuple(78034532224)
    iterate_tuple("tuple")


if __name__ == "__main__":
    main()
