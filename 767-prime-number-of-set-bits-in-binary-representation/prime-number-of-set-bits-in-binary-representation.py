class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0

        for val in range(left, right+1):
            ones = format(val, 'b').count('1')

            if ones in prime_set: 
                count += 1

        return count