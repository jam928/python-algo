def number_of_ways(n: int, x: int) -> int:
    MOD = 10 ** 9 + 7
    memo = {}

    def dfs(n, current_number):
        remainder = n - current_number ** x
        if remainder == 0:
            return 1

        if remainder < 0:
            return 0

        if (remainder, current_number) in memo:
            return memo[(remainder, current_number)]

        result = dfs(n, current_number + 1) + dfs(remainder, current_number + 1)  # include it or not

        memo[(remainder, current_number)] = result
        return result

    return dfs(n, 1) % MOD


print(number_of_ways(n=10, x=2))  # 1
print(number_of_ways(n=4, x=1))  # 2
print(number_of_ways(n=2, x=1))  # 1
print(number_of_ways(n=64, x=3))  # 1
print(number_of_ways(n=213, x=1))  # 55852583
