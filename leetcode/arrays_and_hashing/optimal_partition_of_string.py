# https://leetcode.com/problems/optimal-partition-of-string/

def partition_string(s: str) -> int:
    hashset = set()
    result = 1  # start at 1 since s is a partition

    for c in s:
        if c in hashset:
            result += 1
            hashset = set()

        hashset.add(c)

    return result

if __name__ == '__main__':
    print(partition_string('abacaba')) # 4
    print(partition_string('ssssss')) # 6