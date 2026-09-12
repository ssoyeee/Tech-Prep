class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # finding two nums(a+b) that could equals to k when a+b
        # two pointers
        nums.sort()
        l, r = 0, len(nums)-1
        op = 0

        while l < r:
            if (nums[l] + nums[r]) == k:
                l += 1
                r -= 1
                op += 1

            elif (nums[l] + nums[r]) < k: 
                l += 1
            else: # >k
                r -= 1
        return op
        '''

        nums = [1,2,3,4]
        k = 5
        l = 1
        r = 4
        l+r = 5
        [2, 3]
        l = 2
        r = 3
            = 5

        op = 2
        '''