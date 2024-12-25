from heapq import heapify, heappush, heappop
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        word2count = Counter(s)
        heap = []
        for char, count in word2count.items():
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

        '''
        count = Counter(s) 
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)  

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res
'''
        