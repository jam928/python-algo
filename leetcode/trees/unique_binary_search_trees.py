
# T: O(N^2)
# S: O(N)

# https://leetcode.com/problems/unique-binary-search-trees/

def num_trees(n: int) -> int:
    memo = {}

    def helper(n):
        if n == 0:
            return 1
        elif n == 1 or n == 2:
            return n
        elif n == 3:
            return 5
        elif n in memo:
            return memo[n]
        else:
            result = 0
            for i in range(1, n + 1):
                result += helper(i - 1) * helper(n - i)
            memo[n] = result

        return memo[n]

    return helper(n)