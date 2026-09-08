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

        # Time: O(n) -- where n is len(s) and m is len(shifts), and length of s and shifts are the same, so O(n) + O(n) = O(2n) = O(n)
        # Space: O(n) -- result array