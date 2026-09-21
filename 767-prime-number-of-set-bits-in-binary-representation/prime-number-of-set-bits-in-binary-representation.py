from collections import defaultdict
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        bit_counts = []

        for num in range(left, right + 1):
            ones = format(num, 'b').count('1')
            bit_counts.append(ones)

        for val in bit_counts:
            if val <= 1:
                continue

            limit = int(math.sqrt(val))

            for div in range(2, limit + 1):
                if val % div == 0:
                    break
            else:
                count += 1

        return count
        # Time: O(n * sqrt(B)) -- where B is max set bits, n is right - left+1
        # Space: O(n)