# https://leetcode.com/problems/count-number-of-texts/description/

def count_texts(pressed_keys: str) -> int:
    mod = 1000000007

    memo = {}

    def dfs(index):
        if index >= len(pressed_keys):
            return 1
        if index in memo:
            return memo[index]
        i = index
        count = 0
        counter = 0

        while (i < len(pressed_keys) and
               pressed_keys[i] == pressed_keys[index] and
               ((counter < 3 and pressed_keys[index] != '7' and pressed_keys[index] != '9') or counter < 4 and (
                       pressed_keys[index] == '7' or pressed_keys[index] == '9'))):
            count += dfs(i + 1)
            counter += 1
            i += 1
        memo[index] = count % mod
        return memo[index]

    return dfs(0)

print(count_texts(pressed_keys = "22233")) # 8
print(count_texts(pressed_keys = "222222222222222222222222222222222222")) # 82876089