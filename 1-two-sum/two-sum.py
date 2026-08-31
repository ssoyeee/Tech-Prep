class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
                return [num_map[difference], index]
            else:
                num_map[num] = index