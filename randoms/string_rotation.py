"""String rotation module.
Rotates a given string by n.
"""


def left_shift(value: str, n: int) -> str:
    # rotate given string by n
    # using left shift.
    return value[n:] + value[:n]


def right_shift(value: str, n: int) -> str:
    # rotate given string by n
    # using right shift.
    return value[-n:] + value[:-n]


def main():
    print(left_shift("197", 1))
    print(right_shift("197", 1))


if __name__ == "__main__":
    main()
