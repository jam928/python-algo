# https://leetcode.com/problems/rectangle-area/
# T: O(1)
# S: O(1)

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        points = [Point(ax1, ay1), Point(ax2, ay2), Point(bx1, by1), Point(bx2, by2)]
        
        # calculate area of first and second rectangle
        area1 = abs(points[0].x - points[1].x) * abs(points[0].y - points[1].y)
        area2 = abs(points[2].x - points[3].x) * abs(points[2].y - points[3].y)

        # calculate intersection
        x_dist = min(points[1].x, points[3].x) - max(points[0].x, points[2].x)
        y_dist = min(points[1].y, points[3].y) - max(points[0].y, points[2].y)

        area_i = 0

        if x_dist > 0 and y_dist > 0:
            area_i = x_dist * y_dist

        return (area1 + area2 - area_i)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    s = Solution()
    assert s.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2) == 45
    assert s.computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2) == 16