from collections import defaultdict
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        bi_nums = []

        for i in range(left, right+1):
            binary_clean = format(i, 'b').count('1')
            bi_nums.append(binary_clean)

        for n in bi_nums:
            if n <= 1:
                continue
            limit = int(math.sqrt(n))

            for c in range(2, limit+1):
                if n % c == 0:
                    break
            else:
                count += 1

        return count