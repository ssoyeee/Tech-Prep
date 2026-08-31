class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 수열 찾기
        # set() -> remove duplicates, lookup for O(1)
        num_set = set(nums)
        max_length = 0

        for n in num_set:
            # check if n is the start of a sequence, if n has no predecessor, it starts a new sequence
            if n-1 not in num_set: 
                current = n # start counting from n
                length = 1
                
                while current + 1 in num_set: # while the next number exists
                    current += 1
                    length += 1
                max_length = max(length, max_length)
        return max_length

        # Time: O(n) -- each element is visited at most twice, nested loop still results in linear time
        # Space: O(n) -- the set() stores up to n elements
