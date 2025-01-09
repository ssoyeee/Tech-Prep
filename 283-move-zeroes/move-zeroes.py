class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 1
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            else: nums

               