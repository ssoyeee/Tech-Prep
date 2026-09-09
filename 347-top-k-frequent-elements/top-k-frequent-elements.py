from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counted_nums = Counter(nums)
        heap = []
        for num, count in counted_nums.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]

        # Time: O(n log k) -- Counter build is O(n), heap push/pop ops are O(log k) and when k~n
        # Space: O(n) -- Counter stores up to n unique values; heap adds O(k) but O(n)>O(k)