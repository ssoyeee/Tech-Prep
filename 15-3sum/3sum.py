class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                total = nums[i] + nums[left]+ nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return output
        # Time: O(n^2) -- dominated by O(n^2) -- sort() nlogn + nested loop (O(n) outer x O(n) inner)
        # Space: O(1) in place sort