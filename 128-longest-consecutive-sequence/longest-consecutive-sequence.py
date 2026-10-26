class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n-1 not in num_set: # start point
                length = 1
                while n+1 in num_set:
                    length+=1
                    n+=1
                longest = max(length, longest)

        return longest
        # Time: O(n)
        # Space: O(n)