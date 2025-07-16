from typing import List

from sortedcontainers import SortedDict

# https://leetcode.com/problems/block-placement-queries/description/?envType=company&envId=capital-one&favoriteSlug=capital-one-all
# T: O(NLOGN)
# S: O(NLOGN)
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # {key -> max_size_of_jump(required to pass this point)}
        # use sorted dict for sorted keys
        obstacles = SortedDict()

        result = []

        for query in queries:
            if query[0] == 1:
                # place obstacle in sorted dict map
                index = query[1]

                # find the previous key(lower than index)
                i = obstacles.bisect_left(index)
                prev = obstacles.peekitem(i - 1)[0] if i > 0 else None

                j = obstacles.bisect_right(index)
                next_ = obstacles.peekitem(j)[0] if j < len(obstacles) else None

                if not prev:
                    obstacles[index] = index  # no obstacle to its left so the jump size is the index itself
                else:
                    # set the max jump size as the distance of the previous or the difference between the current index and the prev
                    obstacles[index] = max(index - prev, obstacles[prev])

                # propagete updates to the right if needed
                prev = index
                while next_ and obstacles[next_] > obstacles[prev]:
                    # update next jump requirement if current makes it smaller
                    obstacles[next_] = max(next_ - prev, obstacles[prev])
                    prev = next_
                    j = obstacles.bisect_right(next_)
                    next_ = obstacles.peekitem(j)[0] if j < len(obstacles) else None

            else:
                index = query[1]
                size = query[2]

                if index in obstacles:
                    # theres an obstacle at this index if its max jump is greater the input size
                    result.append(obstacles[index] >= size)
                else:
                    # no obstacle find the closest one to the left
                    i = obstacles.bisect_left(index)
                    prev = obstacles.peekitem(i - 1)[0] if i > 0 else None

                    # no prev so check if the current index is greater than the size
                    if prev is None:
                        result.append(index >= size)
                    else:
                        # Compare against max(index - prev, jump size of prev)
                        result.append(max(index - prev, obstacles[prev]) >= size)

        return result

if __name__ == '__main__':
    s = Solution()
    # print(s.getResults(queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]])) # [False, True, True]
    print(s.getResults(queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]])) # [True, True, False]