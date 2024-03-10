from queue import PriorityQueue


def find_pairs(arr, N):
    """
    :type arr: List[Integer]
    :type N: Integer
    :rtype: List[Integer]
    """
    pq = PriorityQueue()

    def helper(sub_list, index):
        if len(sub_list) == 2:
            diff = abs(sub_list[0] - sub_list[1])
            pq.put((diff, list(sub_list)))

        for i in range(index, len(arr)):
            sub_list.append(arr[i])
            helper(sub_list, i + 1)
            sub_list.pop()

    helper([], 0)

    result = []
    while not pq.empty() and N > 0:
        result.append(pq.get()[0])
        N -= 1
    return result

print(find_pairs([1,5,2], 2))
print(find_pairs([2,5,3,2], 3))