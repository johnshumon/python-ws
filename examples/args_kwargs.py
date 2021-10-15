"""
Args and Kwargs example module
"""


# Note that args is just a name. it can be anything.
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


print(my_sum(1, 2, 3))


def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


def my_sum_unpack(*args):
    result = 0
    for x in args:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

# example of unpack operator
print(my_sum_unpack(*list1, *list2, *list3))


# Example of unpacking operator for dictionary
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
