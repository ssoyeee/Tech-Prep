class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        #check if the first row has zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # check if the first column has zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        # use the 1st row and column as a note
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # set the marked rows to zero
        for r in range(1, rows):
            if matrix[r][0] == 0: # if 1st row marked 
                for c in range(1, cols):
                    matrix[r][c] = 0
        # set the marked columns to zero
        for c in range(1, cols):
            if matrix[0][c] == 0: # if 1st col marked
                for r in range(1, rows):
                    matrix[r][c] = 0

        # set the first row to zero if needed
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0
        
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
        
        return matrix