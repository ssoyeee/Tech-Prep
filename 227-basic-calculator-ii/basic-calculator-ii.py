class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'

        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num*10 + int(ch)
            if (ch in '+-*/') or i==len(s)-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                elif op == '/':
                    stack.append(int(stack.pop()/num))
                op = ch
                num = 0

        return sum(stack)
        # Time: O(n) -- one pass over s, each stack operation is O(1)
        # Space: O(n) -- stack holds up to n/2 numbers
