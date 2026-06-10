from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x+y :
            return False
        return target % gcd(x,y) == 0 #if target is divisible by gcd

        #Bezout's theorem: target must be a multiple of gcd(x, y)

        # T: O(logN) -- gcd calculation
        # S: O(1)