from typing import List


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.nums = nums
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            if 0 < start < self.n - 1 and self.nums[start] > self.nums[start - 1] and self.nums[start] > self.nums[
                start + 1]:
                self.tree[node] = 1
            else:
                self.tree[node] = 0
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, L, R):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_query = self.query(2 * node + 1, start, mid, L, R)
        right_query = self.query(2 * node + 2, mid + 1, end, L, R)
        return left_query + right_query

    def update(self, node, start, end, idx):
        if start == end:
            if 0 < start < self.n - 1 and self.nums[start] > self.nums[start - 1] and self.nums[start] > self.nums[
                start + 1]:
                self.tree[node] = 1
            else:
                self.tree[node] = 0
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(2 * node + 1, start, mid, idx)
            else:
                self.update(2 * node + 2, mid + 1, end, idx)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


def count_of_peaks(nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    seg_tree = SegmentTree(nums)
    results = []

    for query in queries:
        if query[0] == 1: # determine the count of peaks in the nums array
            li, ri = query[1], query[2]
            results.append(seg_tree.query(0, 0, n - 1, li + 1, ri - 1))
        elif query[0] == 2: # update array
            indexi, vali = query[1], query[2]
            nums[indexi] = vali
            seg_tree.update(0, 0, n - 1, indexi)
            if indexi > 0:
                seg_tree.update(0, 0, n - 1, indexi - 1)
            if indexi < n - 1:
                seg_tree.update(0, 0, n - 1, indexi + 1)

    return results

print(count_of_peaks(nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]])) # [0]
print(count_of_peaks(nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]])) # [0,1]