# https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/


# If fed on left then move on
# if no try to feed on the right than the left
# if we cannot , return -1
# Feed the hamster on the right because it can be reused later on for another hamster
def minimum_buckets(hamsters: str) -> int:
    count = 0
    hamsters = list(hamsters)

    for i in range(len(hamsters)):
        if hamsters[i] != 'H':
            continue

        if i >= 0 and hamsters[i - 1] == 'B':
            continue
        elif i + 1 <= len(hamsters) - 1 and hamsters[i + 1] == '.':
            count += 1
            hamsters[i + 1] = 'B'
        elif i - 1 >= 0 and hamsters[i - 1] == '.':
            count += 1
            hamsters[i - 1] = 'B'
        else:
            return -1

    return count

print(minimum_buckets("H..H")) # 2
print(minimum_buckets(".H.H.")) # 1
print(minimum_buckets(".HHH.")) # -1