from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(prefix, nums):
            if not nums: 
                yield prefix
                return
            for index, num in enumerate(nums):
                yield from helper(prefix + [num], nums[:index] + nums[index+1:])
        return list(helper([], nums))
