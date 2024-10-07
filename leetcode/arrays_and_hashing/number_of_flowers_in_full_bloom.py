from functools import cmp_to_key

# T: O(NLOGN) + O(MLOGN)
# S: O(M+N)

# https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/

def compare_func(self, event1, event2):
    # if the time of the events are not equal, then compare the least one
    if event1[1] != event2[1]:
        return event1[1] - event2[1]
    return event1[0] - event2[0]


def full_bloom_flowers(self, flowers, persons):
    # 0 - flower blossoming
    # 1 - person in flower blossom area
    # 2 - flower not blossoming

    # [type of event, time of event]
    arr = []
    for flower in flowers:
        arr.append([0, flower[0]])
        arr.append([2, flower[1]])

    # push persons in the arr as well
    for index, person in enumerate(persons):
        arr.append([1, person, index])

    # sort arr
    arr.sort(key=cmp_to_key(self.compare_func))

    answer = [0 for _ in range(len(persons))]
    flowers_blossom = 0
    for event in arr:
        if event[0] == 0:
            flowers_blossom += 1
        elif event[0] == 2:
            flowers_blossom -= 1
        else:
            answer[event[2]] = flowers_blossom

    return answer

flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]
print(full_bloom_flowers(flowers, people)) # [1,2,2,2]

# flowers = [[1,10],[3,3]]
# people = [3,3,2]
# print(full_bloom_flowers(flowers, people)) # [2,2,1]
