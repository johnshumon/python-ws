"""Example of stack"""
# Tutorial link: https://www.geeksforgeeks.org/stack-in-python/

from collections import deque


def stacks(stack: list) -> None:
    print("pushing to stack")
    stack.append("abu")
    stack.append("john")
    stack.append("crypto")
    stack.append("daneen")

    print("current stack: ", stack)
    print("popping from stack...")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print("stack after popping.: ", stack)


# stack implementation using deque
def deques() -> None:

    stack = deque()

    print("pushing to stack")
    stack.append("abu")
    stack.append("john")
    stack.append("crypto")
    stack.append("daneen")

    print("current stack: ", stack)
    print("popping from stack...")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print("stack after popping.: ", stack)


def main():
    # stacks([])
    deques()


if __name__ == "__main__":
    main()
