class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()[::-1]
        
        return (" ").join(res)