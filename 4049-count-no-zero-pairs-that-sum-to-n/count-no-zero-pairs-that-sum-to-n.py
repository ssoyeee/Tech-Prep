from functools import cache

class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        @cache
        def no_zero(num):
            if num == 0:
                return False

            while num > 0:
                if num % 10 == 0:
                    return False
                num //= 10

            return True

        @cache
        def dfs(i, remain):
            # print("--", i, remain)
            if remain == 0:
                return 1
            if remain < 0:
                return 0

            ways = 0
            digit = remain % 10

            if i > 0:
                # check leading zero
                if digit != 0:
                    ways += 1 if no_zero(remain) else 0

                if remain < 10:
                    ways += 1

            # number 2 have leading zero
            if digit >= 1 and i > 0 and remain > 10:
                ways += 1 if no_zero(remain) else 0

            # check add without carry
            if digit > 1:
                rw = dfs(i + 1, remain // 10)
                ways += (digit - 1) * rw


            # check add with carry
            rw = dfs(i + 1, (remain // 10) - 1)
            ways += (9 - digit) * rw

            return ways

        return dfs(0, n)