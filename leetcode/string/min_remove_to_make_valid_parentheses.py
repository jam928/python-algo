# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# T: O(N)
# S: O(N)
def min_remove_to_make_valid(s: str) -> str:
    # convert to list to easily mark the characters to remove at specific index
    l = list(s)

    # convert string to list to seamless manipulate string
    arr = list(s)

    # keep track of the open count (
    open_count = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            open_count += 1
        elif arr[i] == ')':
            # if we have enough open count decrement it
            if open_count >= 1:
                open_count -= 1
            else:  # we don't have enough open so we must make this closing as a ""
                arr[i] = ""

    for i in range(len(arr) - 1, -1, -1):
        if open_count == 0:
            break
        if arr[i] != '(':
            continue
        arr[i] = ""
        open_count -= 1

    # convert list back to string and return it
    return ''.join(arr)

if __name__ == '__main__':
    print(min_remove_to_make_valid("lee(t(c)o)de)")) # "lee(t(c)o)de"
    print(min_remove_to_make_valid("a)b(c)d")) # "ab(c)d"
    print(min_remove_to_make_valid("))((")) # ""
    print(min_remove_to_make_valid("))(()")) # "()"
    print(min_remove_to_make_valid("())()(((")) # "()()"