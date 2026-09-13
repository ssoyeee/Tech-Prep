class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        op = 0
        left = 0
        right = len(nums)-1
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
        while left < right:
            if nums[left]+nums[right] < k:
                left += 1
            elif nums[left]+nums[right] > k:
                right -= 1
            else:
                op += 1
                left += 1
                right -= 1


        return op