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