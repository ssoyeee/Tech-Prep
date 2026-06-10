class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        max_len = 0
        prefix_sum = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            if prefix_sum in seen:
                max_len = max(max_len, i - seen[prefix_sum])
            else: 
                seen[prefix_sum] = i
        return max_len
        


