""" Checks if a given year is a leap year"""


def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year!")
                return True
            else:
                print(f"{year} is not a leap year.")
                return False
        else:
            print(f"{year} is a leap year.")
            return True
    else:
        print(f"{year} is not a leap year.")
        return False
    return


def main():
    # years = [1700, 1800, 1900, 1988, 1992, 1996, 2000, 2100, 2200, 2300, 2500, 2600]
    years = [1959, 1963, 1971, 1974, 1978, 1982, 1984, 1986, 1990, 2004, 1997, 2020]
    years = [2017, 1900, 2012, 2000]

    for year in years:
        is_leap_year(year)


if __name__ == "__main__":
    main()
