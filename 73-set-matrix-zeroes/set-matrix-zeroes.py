class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in rows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c]=0
        
        # T: O(M*N) -- visit all cells in matrix
        # S: O(M+N) -- 2 sets storing row and col indices