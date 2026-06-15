#from heapq import heapify, heappop, heappush
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
        # T: O(N log K) -- iterate N elements, heap size kept at K (nlargest는 sorted 보다 효율)
        # S: O(N) -- Counter stores all elements

        '''
        num2count = Counter(nums)
        heap = []
        for num, count in num2count.items():
            heap.append((-count, num))
        heapify(heap)
        answer = []
        for _ in range(k):
            _, num = heappop(heap)
            answer.append(num)
        return answer
        '''

        '''
        count = {}
        freq = [[]for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        '''
