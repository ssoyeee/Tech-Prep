class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set() -> search O(1)
        num_set = set(nums)
        max_length = 0

        for n in num_set:
            if n-1 not in num_set:
                current = n
                length = 1
                
                while current + 1 in num_set:
                    current += 1
                    length += 1
                max_length = max(length, max_length)
        return max_length