from typing import List


def eval_rpn(tokens: List[str]) -> int:
    # push each operand to stack and when operator comes evaluate both operands from stack
    # push the result into the stack for the next operation
    stack = []

    # use op map to calculate each of the operators
    op_map = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
        "-": lambda x, y: y - x,
        "/": lambda x, y: y / x
    }

    for c in tokens:
        # if it starts with a - and the rest is numeric or its numeric add to stack
        if (c.startswith("-") and c[1:].isdigit()) or c.isdigit():
            stack.append(int(c))
        # calculate the result from the top two elements in stack with the current operator
        # push the result to stack for next operation
        else:
            result = op_map[c](int(stack.pop()), int(stack.pop()))
            stack.append(int(result))
    return stack[-1]


print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6
print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
