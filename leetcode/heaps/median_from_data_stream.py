import heapq


#
class MedianFinder:

    def __init__(self):
        # maxHeap to store the smaller half of the numbers
        self.maxHeap = []  # maxHeap is implemented as a minHeap with negated values
        # minHeap to store the larger half of the numbers
        self.minHeap = []  # minHeap is a regular min-heap

    # T: O(logn)
    # S: O(n)
    def add_num(self, num: int):
        # Add to minHeap first, then move the smallest value to maxHeap
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        # Balance the heaps if maxHeap has more elements than minHeap
        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    # T: O(1)
    # S: O(n) (no additional space is required beyond the heaps)
    def find_median(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0


if __name__ == '__main__':
    median_finder = MedianFinder()
    median_finder.add_num(1)  # arr = [1]
    median_finder.add_num(2)  # arr = [1, 2]
    print(median_finder.find_median())  # return 1.5 (i.e., (1 + 2) / 2)
    median_finder.add_num(3)  # arr[1, 2, 3]
    print(median_finder.find_median())  # return 2.0
