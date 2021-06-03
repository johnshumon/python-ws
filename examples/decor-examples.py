""" Decorator example"""


def greet(name):
    def get_greet():
        return "Howdy "

    return get_greet() + name


def up(x: int) -> int:
    return x + 1


def down(x: int) -> int:
    return x - 1


def operate(func, x: int) -> int:
    result = func(x)
    return result


def is_called():
    def is_returned():
        return "Returned from is_returned!"

    return is_returned()


def decorate(func):
    def inside_decorate():
        print("Pretty please!")
        func()

    return inside_decorate()


@decorate
def ordinary():
    print("Pretty ordinary")


# printing
# greet_person = greet
# print(greet_person("Daneen"))
# print("output: ", operate(down, 5))
# print(is_called())
ordinary
# pretty = decorate(ordinary)
# pretty()
