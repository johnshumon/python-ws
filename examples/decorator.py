"""Decorator example"""

from functools import wraps


def my_decorator(func_passed_to_dec):
    @wraps(func_passed_to_dec)
    def log_passed_func(*args, **kwargs):

        print(f"{func_passed_to_dec} was called with args={args} and kwargs={kwargs}")

        val = func_passed_to_dec(*args, **kwargs)
        print(f"{func_passed_to_dec} is called with {val}")
        return val

    return log_passed_func


@my_decorator
def hello(a, b):
    print("hello")


a = "hi"
b = "john"
hello(a, b)
