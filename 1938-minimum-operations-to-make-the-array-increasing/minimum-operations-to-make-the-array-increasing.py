class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                ops = (nums[i-1] - nums[i]) + 1
                nums[i] += ops
                operations += ops
        return operations

        