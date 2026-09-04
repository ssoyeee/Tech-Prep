class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rowSum = [sum(row) for row in mat]
        colSum = []
        for j in range(n):
            total = 0
            for i in range(m):
                total += mat[i][j]
            colSum.append(total)
        
        special_count = 0
        for i in range(m):
            for j in range(n):
                if colSum[j]== 1 and rowSum[i]==1 and mat[i][j]==1:
                    special_count +=1
        return special_count

        # Time: O(m*n) -- m rows and n cols
        # Space: O(m+n) -- where len(rowSum) is m and len(colSum) is n