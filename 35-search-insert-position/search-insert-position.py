class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid -1
            else:
                return mid
        return l
        # Time: O(log n)-- cut the search space in half on each iteration
        # Space: O(1)
