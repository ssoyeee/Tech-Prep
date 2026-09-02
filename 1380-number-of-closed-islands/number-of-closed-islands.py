class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False # out of bounds - this dir is open 
            if grid[row][col] == 1:
                return True # hit water - this dir is closed off
            
            grid[row][col] = 1 # mark visited
            
            top = dfs(row-1, col)
            bottom = dfs(row+1, col)
            left = dfs(row, col-1)
            right = dfs(row, col+1)
            
            return top and bottom and left and right # closed only if 4 dir are closed

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1
        return count
            
