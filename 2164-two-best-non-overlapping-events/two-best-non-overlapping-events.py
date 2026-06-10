import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        max_val = 0
        result = 0
    
        for start, end, val in events:
            # pop events that ended before current start
            while heap and heap[0][0] < start:
                _, v = heapq.heappop(heap)
                max_val = max(max_val, v)
        
            # current event + best previous event
            result = max(result, val + max_val)
        
            # push current event for future use
            heapq.heappush(heap, (end, val))
    
        return result

    # T: O(N log N) -- sorting + heap operations
    # S: O(N) -- heap stores all events