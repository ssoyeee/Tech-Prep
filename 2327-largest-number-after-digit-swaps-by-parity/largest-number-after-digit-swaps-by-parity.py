class Solution:
    def largestInteger(self, num: int) -> int:
        arr = list(map(int, str(num)))

        even_max_heap = []  
        odd_max_heap = []  

        # Populate the heaps
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                heapq.heappush(even_max_heap, (-arr[i], i))  
            else:
                heapq.heappush(odd_max_heap, (-arr[i], i))

        ans = []

        # Construct the result
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                _, index = heapq.heappop(even_max_heap)
                ans.append(arr[index])
            else:
                _, index = heapq.heappop(odd_max_heap)
                ans.append(arr[index])

        return int(''.join(map(str,ans)))
