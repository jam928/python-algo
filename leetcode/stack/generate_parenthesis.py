from typing import List


# https://leetcode.com/problems/generate-parentheses/description/
# T: O(4^n / sqrt(n))
# S: O(4^n / sqrt(n))
def generate_parenthesis(n: int) -> List[str]:
    result = []

    def dfs(s, open_count, close_count):
        # if the number of open parenthesis and close are the same as n;
        # then add all the elements from the stack to the results arr
        if open_count == n and close_count == n:
            result.append(s)
            return

        # if the number open parenthesis is less than n; append to
        if open_count < n:
            dfs(s + '(', open_count + 1, close_count)

        # push an close parenthesis if its less than the current open count
        if close_count < open_count:
            dfs(s + ')', open_count, close_count + 1)

    dfs('', 0, 0)
    return result


print(generate_parenthesis(3))
print(generate_parenthesis(1))
print(generate_parenthesis(8))
