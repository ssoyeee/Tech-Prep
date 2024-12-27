class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(open, close):
            if open == 0 and close == 0:
                yield ""
                return
            if open:
                for p in helper(open-1, close):
                    yield "(" +p
            if open < close: 
                for p in helper(open, close-1):
                    yield ")" + p
        return list(helper(n, n))