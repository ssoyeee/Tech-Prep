class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        # Step 1: scan from the right to find the first index i
        # where nums[i] < nums[i+1] (where ascending order breaks)
        i = n-2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # If i is -1, the whole array is in descending order (it's largest permutation), 
        # so we skip swapping and just reverse below
        if i >= 0:
            # Step 2: find the smallest value to the right of i 
            # that is still greater than nums[i] (scan from the right since that part is desc, 
            # so the first value bigger than nums[i] is the smallest such value)
            j = n - 1 
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i] # swap

        # Step 3: everything after i is still in descending order,
        # reverse it to get the smallest possible arrangement
        nums[i+1:] = reversed(nums[i+1:])     