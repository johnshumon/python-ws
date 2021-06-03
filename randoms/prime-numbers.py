"""Checks prime number"""


def is_prime_number(number: int) -> bool:
    if (number <= 1):
        return False
    else:
        for element in range(2, number):
            if number % element == 0:
                return False

        return True


def main():
    for i in range(20):
        if (is_prime_number(i)):
            print("{0}: prime".format(i))
        else:
            print("{0}: not prime".format(i))


if __name__ == "__main__":
    main()
