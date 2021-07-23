"""Set module
This module contains basic examples
of set along with some set operations
"""

# > Sets are unordered.
# > Set elements are unique. Duplicate elements are not allowed.
# > A set itself may be modified, but the elements contained in
#   the set must be of an immutable type.
# > An empty set is falsy in a Boolean context
#
# A set can be created in two ways.
# > x = set(<iter>)
#   x = {<obj>, <obj>, ..., <obj>}


def sets() -> None:
    # list to set
    x = set(["foo", "bar", "baz", "foo", "qux"])
    print("list->set: {}".format(x))

    # tuple to set
    x = set(("foo", "bar", "baz", "foo", "qux"))
    print("tuple->set: {}".format(x))

    # set size and membership
    print("size: {}".format(len(x)))
    print("bar" in x)

    # elements in a set can be objects of different types
    # > set elements must be immutable i.e. list/dictonary
    # can be a set element but tuple can.
    x = {42, "foo", 3.14159, None, (1, 2, 3)}

    # union: x1.union(x2[, x3 ...])
    # > option 1: x1.union(x2, x3)
    # > option 2: a | b | c | d
    x1 = {1, 2, 3, 4}
    x2 = {2, 3, 4, 5}
    x3 = {3, 4, 5, 6}
    print("x1.union(x2, x3): {}".format(x1.union(x2, x3)))

    # intersection: x1.intersection(x2[, x3 ...])
    # > option 1: x1.intersection(x2, x3)
    # > option 2: x1 & x2 & x3
    print("x1.intersection(x2, x3): {}".format(x1.intersection(x2, x3)))

    # difference: x1.difference(x2[, x3 ...])
    # When multiple sets are specified, the operation is
    # performed from left to right. i.e. x1 - x2 -> result
    # then result - x3
    #
    # > option 1: x1.difference(x2, x3)
    # > option 2: x1 - x2 - x3
    print("x1.difference(x2, x3): {}".format(x1.difference(x2, x3)))

    # symmetric_difference x1 ^ x2 [^ x3 ...]
    # for more than 2 sets use option 2 as
    # symmetric_difference takes only 1 args
    # > option 1: x1.symmetric_difference(x2)
    # > option 2: x1 ^ x2 ^ x3
    print("x1 ^ x2 ^ x3): {}".format(x1 ^ x2 ^ x3))

    # OTHER FUNCTIONS
    # > x1.isdisjoint(x2)
    # > x1.issubset(x2)
    # > x1.issuperset(x2)

    # MODIFYING A SET
    # x1.update(x2[, x3 ...])
    # x1 |= x2 [| x3 ...]
    # add to x1 any elements in x2 that x1 does not already have
    x1 |= x2
    print("x1 |= x2: {}".format(x1))


def main():
    sets()


if __name__ == "__main__":
    main()
