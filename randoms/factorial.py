"""Returns factorial of a number"""


def factorial(number: int) -> int:
    if (number == 0 or number == 1):
        return 1
    else:
        return number * factorial(number - 1)


def main():
    number = factorial(6)
    print(number)


if __name__ == "__main__":
    main()
