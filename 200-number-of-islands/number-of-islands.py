class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
        #base case
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col]=='0':
                return
            grid[row][col] = '0'

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count
        

        
        '''
        # 1) boundary
        # 2) water
        # 3) mark visited
        # 4) 4 directions

        if not grid or not grid[0]:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if r <0 or c<0 or r>=rows or c>=cols:
                return

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count
        '''