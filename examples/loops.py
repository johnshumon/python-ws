"""Loops in python"""


def loops(arr: list) -> None:
    # i is an integer, can access the list element with arr[i]
    print("for i in range...")
    for i in range(len(arr)):
        print(arr[i])

    # element refers to the element in the list, i.e. it is the same as arr[i]
    print("for element in arr...")
    for element in arr:
        print(element)

    # if you want to skip the the first element, you can slice the list [tutorial]:
    print("for element in arr[1:]")
    for element in arr[1:]:
        print(element)

    # break example
    print("break example...")
    for element in arr:
        print(element)
        if (element < 0):
            print("negative number")
            break

    # while loop
    print("while element in arr")
    i = 0
    while i < len(arr):
        print(arr[i])
        i = i + 1


def main():
    loops([1, 2, 3, 5, -1, 7, 11, 13, 17])


if __name__ == "__main__":
    main()
