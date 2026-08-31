class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix sum: 각 위치까지의 누적합
        count = 0
        curr_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        
        for num in nums:
            curr_sum += num
            count += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] += 1
        return count