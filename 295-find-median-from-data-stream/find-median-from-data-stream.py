
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.max_heap = [] # Max heap for the smaller half of the numbers
        self.min_heap = [] # Min heap for the larger half of the numbers

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num) # Add to max heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            heappush(self.min_heap, -heappop(self.max_heap))
        
        if len(self.max_heap) > len(self.min_heap) + 1: # difference 1 (if diff is larger than 1, can miss some value)
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap): 
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()