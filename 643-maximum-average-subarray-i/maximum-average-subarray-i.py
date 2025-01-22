class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        i, j = 0, 0
        cur_sum = 0
        max_avg = float('-inf')

        while j<n:
            cur_sum += nums[j]
            if j-i+1 == k:
                max_avg = max(max_avg, cur_sum/k)
                cur_sum -= nums[i]
                i += 1
            j += 1
        return max_avg
        # Time: O(N) where N is length of nums
        # Space: O(1)
