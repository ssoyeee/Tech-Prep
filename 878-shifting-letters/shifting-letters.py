class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        for i in range(len(shifts)-1, -1, -1):
            total += shifts[i]
            shifts[i] = total
        result = []
        for i in range(len(s)):
            new_index = ((ord(s[i]) - ord('a'))+shifts[i]) % 26
            result.append(chr(new_index + ord('a')))
        return ''.join(result)