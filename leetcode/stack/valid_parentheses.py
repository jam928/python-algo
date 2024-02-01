def is_valid(s: str) -> bool:
    # store elements in stack
    char_stack = []

    for c in s:
        # if its opening character append to stack and continue to next iteration
        if c == '(' or c == '[' or c == '{':
            char_stack.append(c)
            continue

        # if its a closing char and stack is empty then we cant compare and return false
        if len(char_stack) == 0:
            return False

        last_char = char_stack.pop()
        # return false if no match
        if c == ')' and last_char != '(':
            return False
        if c == '}' and last_char != '{':
            return False
        if c == ']' and last_char != '[':
            return False

    return len(char_stack) == 0

print(is_valid(s = "()")) # true
print(is_valid(s = "()[]{}")) # true
print(is_valid(s = "(]")) # false
