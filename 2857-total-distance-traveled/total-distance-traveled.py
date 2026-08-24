class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total = mainTank # total liter 
        while mainTank >= 5:
            mainTank -= 5
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
                total += 1
        return total * 10