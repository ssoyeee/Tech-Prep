class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        left, right = 1, max(ribbons)+1

        while left < right:
            mid = (left+right) //2
            if self.can_cut(ribbons, mid, k):
                left = mid + 1
            else:
                right = mid
        return left -1

    def can_cut(self, ribbons: list[int], length: int, k: int) -> bool:
        count = 0
        for ribbon in ribbons:
            count += ribbon//length
        return count >= k

    #Time: O(n log M) -- where M is max(ribbons) and n is len(ribbons), 
    #                   (binary search runs logM times, each can_cut scans n ribbons)
    #Space: O(1)

    # Pattern
    # Find Last 'O' left = mid, right=mid-1, round-up mid, return left
    # Find First 'X' right = mid, left = mid+1, round-down mid, return left