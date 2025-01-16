from typing import List


# T: O((N ^ 2) * M)
# S: O(N)

# https://leetcode.com/problems/similar-string-groups/description/
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups = 0
        n = len(strs)
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue
            groups += 1
            arr = [strs[i]]
            self.dfs(i, strs, visited, arr)

        return groups

    def dfs(self, i, strs, visited, arr):
        visited[i] = True
        for j in range(len(strs)):
            if visited[j]:
                continue
            if self.isSimilar(strs[i], strs[j]):
                arr.append(strs[j])
                self.dfs(j, strs, visited, arr)

    def isSimilar(self, a, b):
        mis_matched = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                mis_matched += 1

        return mis_matched == 2 or mis_matched == 0

if __name__ == '__main__':
    sol = Solution()
    strs = ["tars","rats","arts","star"]
    print(sol.numSimilarGroups(strs)) # 2

    strs = ["omv","ovm"]
    print(sol.numSimilarGroups(strs)) # 1

    strs = ["blw", "bwl", "wlb"]
    print(sol.numSimilarGroups(strs)) # 1