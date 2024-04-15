from typing import List

# https://leetcode.com/problems/detect-squares/

class DetectSquares:
    def __init__(self):
        self.freq_map = {}
        self.points = []

    # T: O(1)
    # S: O(1)
    def add(self, point: List[int]) -> None:
        tuple_point = (point[0], point[1])
        self.freq_map[tuple_point] = self.freq_map.get(tuple_point, 0) + 1
        self.points.append(point)

    # T: O(N)
    # S: O(1)
    def count(self, point: List[int]) -> int:
        x1 = point[0]
        y1 = point[1]
        count = 0
        for i in range(len(self.points)):
            x2 = self.points[i][0]
            y2 = self.points[i][1]

            # skip if its not on the diagonal or if its the same point in question
            if abs(y1 - y2) != abs(x1 - x2) or x1 == x2 or y1 == y2:
                continue

            # if its in the diagonal and the other points exist in map, add to count
            if (x1, y2) in self.freq_map and (x2, y1) in self.freq_map:
                count += self.freq_map[(x1, y2)] * self.freq_map[(x2, y1)]

        return count


if __name__ == '__main__':
    detect_squares = DetectSquares()
    detect_squares.add([3, 10])
    detect_squares.add([11, 2])
    detect_squares.add([3, 2])

    print(detect_squares.count([11, 10]))  # 1
    print(detect_squares.count([14, 8]))  # 0

    detect_squares.add([11, 2])

    print(detect_squares.count([11, 10]))  # 2
