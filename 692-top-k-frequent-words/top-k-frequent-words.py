from heapq import heappop, heapify
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word2count = Counter(words)
        heap = []
        for word, count in word2count.items():
            heap.append((-count, word)) # maxheap
        heapify(heap)
        answer = []
        for _ in range(k):
            _, word = heappop(heap)
            answer.append(word)
        return answer
       
    '''
       # error checking
        if not words or k <=0:
            return []
        
        #create dictionary:
        wordsDict={}
        for word in words:
            if word in wordsDict:
                wordsDict[word] += 1
            else:
                wordsDict[word] =1 
        
        #create heap
        heap = [(-freq, word) for word, freq in wordsDict.items()]
        heapq.heapify(heap) #not using extra memory
        
        
        # return top k results from heap
        return [heapq.heappop(heap)[1] for _ in range(k)] #[1] menas : not the frequency, just the word
        '''