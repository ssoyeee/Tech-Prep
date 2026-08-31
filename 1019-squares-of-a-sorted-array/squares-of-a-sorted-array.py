
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = []
        # for i in range(0,len(nums)):
        #     res.append(pow(nums[i],2))
        # return sorted(res)     
        n = len(nums)
        left, right = 0, n-1
        result = [0] * n
        pos = n - 1

        while left<right:
            if nums[left]**2 > nums[right]**2:
                result[pos] = nums[left]**2
                left += 1
            else:
                result[pos] = nums[right]**2
                right -= 1
            pos -= 1
        # left == right
        result[pos] = nums[left]**2
        return result
        # two pointer O(n)
        # Time: O(n)