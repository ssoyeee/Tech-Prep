from heapq import heapify, heappush, heappop
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        char2count = Counter(s)
        heap = []
        for char, count in char2count.items():
            heap.append([-count, char])
        heapify(heap) # avg: O(n)
        answer = ''
        prev = None # not to use it twice in a row
        while heap or prev:
            if prev and not heap:
                return ""
            # most frequent, except prev
            count, char = heappop(heap)
            answer += char
            count += 1 # count is negative so increment by +1
            if prev:
                heappush(heap, prev)
                prev = None
            if count != 0:
                prev = [count, char]

        return answer