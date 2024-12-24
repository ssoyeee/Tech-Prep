class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(abs(x-element), element) for element in arr] 
        heapify(heap)
        answer = []
        for _ in range(k):
            _, element = heappop(heap)
            answer.append(element)
        return sorted(answer)