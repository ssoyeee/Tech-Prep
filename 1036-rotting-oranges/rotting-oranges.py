class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))      
        minutes = 0
        directions = [(-1,0),(0,-1),(1,0),(0,1)] #u, l, d, r

        while queue and fresh > 0:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()

                for dx, dy in directions:
                    newRow, newCol = row + dx, col + dy
                    if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == 1:
                        queue.append((newRow, newCol))
                        fresh -= 1
                        grid[newRow][newCol] = 2
            minutes += 1
        return minutes if fresh == 0 else -1  
        '''
        row, col = len(grid), len(grid[0])
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        new_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while fresh:
            if not rotten: 
                return -1
            rotten = {(i+di, j+dj) for i, j in rotten for di, dj in new_dir if (i+di, j+dj) in fresh}
            fresh -= rotten
            timer += 1
        return timer
        '''

        # Time O(m*n) where m, n are the number of rows and col
        # Space O(m*n) in worst case, when all org are fresh