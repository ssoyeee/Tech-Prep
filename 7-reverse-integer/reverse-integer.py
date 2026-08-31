class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x<0
        x = abs(x)

        reversed_integer = 0 
        while x > 0:
            last_digit = x % 10
            reversed_integer = reversed_integer * 10 + last_digit
            x = x // 10
        
        if is_negative:
            reversed_integer = -reversed_integer

        if reversed_integer < -2**31 or reversed_integer > 2**31 - 1:
            return 0
        return reversed_integer

        # Time: O(log x) -- since we process one digit per iteration, x has about log base 10 of x digits
        # Space: O(1) -- since we only use a fixed number of variables