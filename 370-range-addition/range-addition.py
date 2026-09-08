class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # difference array
        diff = [0] * length
        for start, end, inc in updates:
            diff[start] += inc
            if end+1<length:
                diff[end+1] -= inc # cancel out after end

        arr = [0] * length
        arr[0] = diff[0]
        for i in range(1, length):
            arr[i] = arr[i-1]+diff[i]
        return arr
        # brute-force: Time O(m * n)
        
        # difference array + prefix sum
        # Time: O(m+n) -- where m is len(updates), n is length
        # Space: O(n) -- diff and arr arrays