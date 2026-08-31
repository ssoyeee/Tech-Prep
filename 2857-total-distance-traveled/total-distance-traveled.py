class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total_used = 0
        while mainTank >= 5:
            mainTank -= 5
            total_used += 5
            if additionalTank >= 1:
                additionalTank -=1
                mainTank += 1
        total_used += mainTank
        return total_used * 10

        # Time: O(n) -- where n is mainTank's value
        # Space: O(1) -- only use constant number of variables