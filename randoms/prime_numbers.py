"""Checks prime number"""


def get_primes(limit: int = 1000000) -> list:
    """Returns list of primes for a given limit"""

    # Return all between 2 to below 1
    # million. Empty list otherwise
    if limit < 2 or limit > 10 ** 6:
        return []

    prime_sieve = [True] * limit

    # limit**0.5 -> square root of limit
    # + 1 for celling value
    for i in range(2, (int(limit ** 0.5) + 1)):
        if prime_sieve[i]:
            for j in range(i * i, limit, i):
                prime_sieve[j] = False

    return [prime for prime in range(2, limit) if prime_sieve[prime]]


def is_prime_number(number: int) -> bool:
    primes = get_primes()

    return True if number in primes else False


def main():
    input_number = int(input("Enter a number below 1000000 to see if it's a prime: "))

    if is_prime_number(input_number):
        print("{} is a prime".format(input_number))
    else:
        print("{} is not a prime".format(input_number))

    input_number = int(input("Enter a number below 1000000: "))
    primes = get_primes(input_number)
    print("All prime below {} are: {}".format(input_number, primes))


if __name__ == "__main__":
    main()
