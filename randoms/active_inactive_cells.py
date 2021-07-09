# Given a binary array of size n where n > 3. A true (or 1)
# value in the array means active and false (or 0) means
# inactive.
#
# > Given a number k, the task is to find count of
# active and inactive cells after k days. After every day,
# status of i’th cell becomes
# > active(i.e. 1) -> if left and right cells are different
#   inactive(i.e. 0) -> if left and right cell are same
#  (both 0 or both 1).
#
# Since there are no cells before leftmost and after rightmost
# cells, the value cells before leftmost and after rightmost
# cells is always considered as 0 (or inactive).

from typing import List


def cell_complete(states: List[int], days: int) -> List[int]:

    states_holder = [None] * len(states)

    j = 0
    while j < days:
        for index in range(len(states)):
            left_edge = 0 if index == 0 else states[index - 1]
            right_edge = 0 if index == (len(states) - 1) else states[index + 1]
            states_holder[index] = 0 if left_edge == right_edge else 1

        states = states_holder
        j = j + 1

    return states


def main():
    init_state = [1, 0, 0, 0, 0, 1, 0, 0]
    result = cell_complete(init_state, 1)

    print("initial: {}".format(init_state))
    print("result: {}".format(result))


if __name__ == "__main__":
    main()
