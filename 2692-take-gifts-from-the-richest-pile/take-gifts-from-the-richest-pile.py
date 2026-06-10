import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            max_val = -heapq.heappop(heap)
            new_val = math.floor(math.sqrt(max_val))
            heapq.heappush(heap, -new_val)
        return sum(-g for g in heap)