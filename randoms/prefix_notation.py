"""Prefix notation module"""

from typing import Any, Dict


def calculate(operator: str, operand_1: int, operand_2: int) -> int:

    if operator == "+":
        return operand_1 + operand_2
    elif operator == "-":
        return operand_1 - operand_2
    elif operator == "*":
        return operand_1 * operand_2
    elif operator == "/":
        if operand_1 < 0 < operand_2 or operand_1 > 0 > operand_2:
            return -(abs(operand_1) // abs(operand_2))
        return operand_1 // operand_2


def get_variable_values(variables: Dict) -> Dict:
    for key, value in variables.items():
        # If value of the key is a tuple then this picks
        # maximum value by setting tuple values are the
        # lower and upper bound of a range.
        if isinstance(value, tuple):
            variables[key] = max(item for item in range(value[0], value[1]))

    return variables


def parse(expression: str, *args) -> Any:

    # Sanity for empty expression
    if expression is None or expression == "" or expression == " ":
        return None

    # Expression is split and tokenized.
    tokens = [value for value in reversed(expression.split(" ")) if value != ""]
    result = []
    variables = {}

    # If expression contains variables it's passed
    # as an dictionary argument. This checks if there
    # is valid arguments.
    if args:
        for item in args:
            variables = item

        if isinstance(variables, dict):
            get_variable_values(variables)

        for i in range(len(tokens)):
            if tokens[i] in variables:
                tokens[i] = str(variables[tokens[i]])

    # Any tokenized list length less than 3
    # doesn't form a valid expression.
    if len(tokens) < 3:
        return None

    for token in tokens:
        if token in "+-*/":
            op_1, op_2 = result.pop(), result.pop()
            result.append(calculate(token, op_1, op_2))
        # Handles tokens with negative values e.g. -11
        elif token.lstrip("-").isdigit():
            result.append(int(token))
        else:
            return None

    return result[-1] if len(result) == 1 and result[-1] != 0 else None


if __name__ == "__main__":
    assert parse("+ 1 5") == 6
    assert parse("+ 1 2 3") is None
    assert parse("+ 1 ") is None
    assert parse("9") is None
    assert parse("- * + 1 2 3 4") == 5
    assert parse("-+1 5 3") is None
    assert parse("+ 1      2") == 3
    assert parse("+ 6 * - 4 + 2 3 8") == -2
    assert parse("/ 15 - 6 3") == 5
    assert parse("* + 2 x y", {"x": (0, 2), "y": (2, 4)}) == 9
    assert parse("* + 2 x y", {"x": 1, "y": 3}) == 9

    print(parse("+ 1 5"))
    print(parse("+ 1 2 3"))
    print(parse("+ 1"))
    print(parse("+ / 5 13 4"))
    print(parse("9"))
    print(parse("-+1 5 3"))
    print(parse("+ 1       2"))
    print(parse("+ 6 * - 4 + 2 3 8"))
    print(parse("/ 15 - 6 3"))
    print(parse("* + 2 x y", {"x": (0, 2), "y": (2, 4)}))
    print(parse("* + 2 x y", {"x": 1, "y": 3}))
