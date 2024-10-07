from typing import List

# https://leetcode.com/problems/image-overlap/

def largestOverlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    set_img1 = set()
    set_img2 = set()

    for i in range(len(img1)):
        for j in range(len(img1)):
            if img1[i][j]:
                set_img1.add((i, j))
            if img2[i][j]:
                set_img2.add((i, j))

    result = 0

    for i in range(-(len(img1) - 1), len(img1)):
        for j in range(-(len(img1) - 1), len(img1)):
            count = 0
            for e in set_img1:
                x, y = e
                if (x + i, y + j) in set_img2:
                    count += 1
            result = max(result, count)

    return result