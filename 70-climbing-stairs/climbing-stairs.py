class Solution:
    def climbStairs(self, n: int) -> int:
        # fibo, dp
        
        # base case
        if n == 1: return 1
        if n == 2: return 2

        prev, curr = 1, 2
        for _ in range(3, n+1):
            prev, curr = curr, prev+curr
        return curr
        
# T: O(N) -- iterate N steps
# S: O(1) -- only two variables prev and curr