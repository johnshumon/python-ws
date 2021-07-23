"""Utility module.
This module contains mixed example
of useful python tutorials and code
snippets.
"""


def double_dash() -> None:
    # single "/" and double "//"
    # slash operator
    # > /: float value
    #   //: floar/interger value

    flaot_val = 8 / 3
    int_val = 8 // 3
    print("8/3: {0:.3f} -- ".format(flaot_val), "8//3: {}".format(int_val))
    # print("8/3: {} - 8//3: {}".format(flaot_val, int_val))


def main():
    double_dash()


if __name__ == "__main__":
    main()
