
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.max_heap = [] # Max heap for the smaller half of the numbers
        self.min_heap = [] # Min heap for the larger half of the numbers

    def addNum(self, num: int) -> None: #T: O(logn)-heap
        heappush(self.max_heap, -num) # Add to max heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]): 
            # min_heap and max_heap exist, 
            # maximum value of max_heap(means smallest) is larger than minimum of min_heap, update it.
            heappush(self.min_heap, -heappop(self.max_heap))

        # difference 1 (if diff is larger than 1, can miss some value)
        if len(self.max_heap) > len(self.min_heap) + 1: 
            #max_heap(has more)->min_heap
            heappush(self.min_heap, -heappop(self.max_heap))
        # vice versa
        elif len(self.min_heap) > len(self.max_heap): 
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float: #T:O(1)- access heap root
        # if length of heap is the same, median is average of two heap[0]
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # otherwise, max_heap[0] which means median,
        # ex: max_heap[-2, -1], min_heap[3] -> median [2]
        return -self.max_heap[0]
#space: O(n) -total number of elements stored
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()