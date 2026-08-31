class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_result = [x**2 for x in nums]
        return sorted(squared_result)
        
        # Time: O(n log n) -- uses sorted()
        # --> with Two Pointer, O(n)