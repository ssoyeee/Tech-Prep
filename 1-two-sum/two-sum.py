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


        # Time: O(n) -- single pass through nums, each hashmap operation is O(1) 
        # Space: O(n) -- in worst, num_map can have up to n-1 elements