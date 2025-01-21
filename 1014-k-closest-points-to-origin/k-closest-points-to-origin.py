class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []  #smallest-closest
        for point in points:
            distance = -(point[0] ** 2 + point[1] ** 2)  # negative because of maxheap
            heapq.heappush(max_heap, (distance, point)) # in Python, heappush - sorted by 1st element in tuple
            if len(max_heap) > k:
                heapq.heappop(max_heap)  

        return [item[1] for item in max_heap]  #return point
        # Time: O(N*log K) where N is the number of list points , K is size of heap
        # Space: O(K) where k is maximum heap size