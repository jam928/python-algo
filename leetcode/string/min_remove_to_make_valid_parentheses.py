# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

def min_remove_to_make_valid(s: str) -> str:
    # convert to list to easily mark the characters to remove at specific index
    l = list(s)

    open_count = close_count = 0

    for index, c in enumerate(l):

        if c == '(':
            open_count += 1
        elif c == ')':
            if open_count > 0:
                open_count -= 1
            else:
                l[index] = ""
            close_count += 1

    # remove the remaining characters from back to front that are left open (
    if open_count > 0:
        for i in range(len(l) - 1, -1, -1):
            if l[i] == '(':
                l[i] = ""
                open_count -= 1

            if open_count == 0:
                break
    # convert list back to string
    s = "".join(l)

    return s

if __name__ == '__main__':
    print(min_remove_to_make_valid("lee(t(c)o)de)")) # "lee(t(c)o)de"
    print(min_remove_to_make_valid("a)b(c)d")) # "ab(c)d"
    print(min_remove_to_make_valid("))((")) # ""
    print(min_remove_to_make_valid("))(()")) # "()"
    print(min_remove_to_make_valid("())()(((")) # "()()"