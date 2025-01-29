class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        i, j, total_sum, result = 0, 0, 0, 0
        while j<n:
            total_sum += arr[j]
            if j-i+1 == k:
                if total_sum/k >= threshold:
                    result += 1
                total_sum -= arr[i]
                i +=1
            j+=1
        return result