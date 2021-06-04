"""Calculate simple interest"""

HUNDRED = 100


def simple_interest(p: int, t: int, r: int) -> float:
    # P -> principle amount
    # T -> the time and
    # R -> the rate
    return (p * t * r) / HUNDRED


def main():
    print(simple_interest(10000, 5, 5))
    print(simple_interest(8, 6, 8))
    print(simple_interest(3000, 1, 7))


if __name__ == "__main__":
    main()
