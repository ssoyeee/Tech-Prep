class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        value = nums[0]
        for n in nums:
            if abs(n) < abs(value):
                value = n
            elif abs(n) == abs(value):
                if n > value:
                    value = n
        return value