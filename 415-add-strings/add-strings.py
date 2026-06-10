class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # reversed calculation 
        i = len(num1)-1
        j = len(num2)-1
        result = []
        carry = 0

        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            total = d1 + d2 + carry
            carry = total // 10
            digit = total % 10
            result.append(str(digit))

            i -= 1
            j -= 1
        return ''.join(reversed(result))

        # T: O(N) -- N is max len of num1 and num2
        # S: O(N) -- result arr stores each digit