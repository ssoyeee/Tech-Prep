class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_len = 0
        prefix_sum = 0
        seen = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum-k in seen:
                max_len = max(max_len, i-seen[prefix_sum-k])
            if prefix_sum not in seen:
                seen[prefix_sum] = i
        return max_len
        # T: O(N) -- one pass with hashmap lookup O(1)
        # S: O(N) -- seen hashmap
