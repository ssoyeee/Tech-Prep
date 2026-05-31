class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 2d dp
        result = []
        for i in range(numRows):
            curr = [1] * (i+1) # initialize row with 1s
            if i > 0: # skip 1st row, no prev row exists
                prev = result[i-1]
                for j in range(1, len(curr)-1):
                    curr[j] = prev[j-1]+prev[j]
            result.append(curr)
        return result

        # T: O(N^2)--- N rows, each row up to N elements
        # S: O(N^2)--- storing all rows in result 