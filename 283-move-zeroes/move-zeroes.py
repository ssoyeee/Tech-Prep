class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = 0
        # move all non-zero to the front
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[cur], nums[non_zero] = nums[non_zero], nums[cur]
                non_zero += 1
        # return updated nums
        return nums
        #Time: O(n)
        #Space: O(1)