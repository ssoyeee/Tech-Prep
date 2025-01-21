class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []  #smallest-closest
        for point in points:
            distance = -(point[0] ** 2 + point[1] ** 2)  # negative because of maxheap
            heapq.heappush(max_heap, (distance, point)) 
            if len(max_heap) > k:
                heapq.heappop(max_heap)  

        return [item[1] for item in max_heap]  #return point