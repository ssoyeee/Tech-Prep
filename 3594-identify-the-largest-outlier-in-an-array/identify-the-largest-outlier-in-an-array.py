from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        count = Counter(nums)
        max_outlier = float('-inf')
        
        for candidate in nums:
            outlier = total - 2 * candidate
            if outlier in count:
               if outlier != candidate or count[outlier] > 1:
                    max_outlier = max(max_outlier, outlier)
        return max_outlier   

        # T: O(N) -- one pass
        # S: O(N) -- Counter hashmap