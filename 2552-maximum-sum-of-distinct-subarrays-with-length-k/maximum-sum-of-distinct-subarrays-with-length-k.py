class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num2count = defaultdict(int)
        n = len(nums)
        i, j, cur_sum, max_sum= 0, 0, 0, 0
        while j<n:
            cur_sum += nums[j]
            num2count[nums[j]] += 1
            if j-i+1 == k:
                if len(num2count) == k:
                    max_sum = max(max_sum, cur_sum)   
                start_num = nums[i]
                cur_sum -= start_num
                num2count[start_num] -= 1
                if num2count[start_num] == 0:
                    del num2count[start_num]
                i += 1
            j += 1
        return max_sum
        # Time O(N) Space O(N)