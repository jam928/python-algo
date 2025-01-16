import heapq


#
class MedianFinder:

    def __init__(self):
        # maxHeap to store the smaller half of the numbers
        self.max_heap = []  # maxHeap is implemented as a minHeap with negated values
        # minHeap to store the larger half of the numbers
        self.min_heap = []  # minHeap is a regular min-heap

    # T: O(logn)
    # S: O(n)
    def add_num(self, num: int):
        # Add to minHeap first, then move the smallest value to maxHeap
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        # Balance the heaps if maxHeap has more elements than minHeap
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    # T: O(1)
    # S: O(n) (no additional space is required beyond the heaps)
    def find_median(self) -> float:
        # if the length of the min heap is greater than the max heap
        # return the first element in the min heap
        if len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])

        # return the difference of both heaps
        return (self.min_heap[0] - self.max_heap[0]) / 2.0

if __name__ == '__main__':
    median_finder = MedianFinder()
    median_finder.add_num(1)  # arr = [1]
    median_finder.add_num(2)  # arr = [1, 2]
    print(median_finder.find_median())  # return 1.5 (i.e., (1 + 2) / 2)
    median_finder.add_num(3)  # arr[1, 2, 3]
    print(median_finder.find_median())  # return 2.0