class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited_set  = set()
        res = False
        
        def dfs(i,j,visited_set,word,index):
            if index == len(word):
                return True
            if i<0 or i>m-1 or j <0 or j>n-1 or (i,j) in visited_set or word[index] != board[i][j]:
                return False
            visited_set.add((i,j))

            res = (dfs(i+1,j,visited_set,word,index+1) or 
            dfs(i,j+1,visited_set,word,index+1) or
            dfs(i-1,j,visited_set,word,index+1) or
            dfs(i,j-1,visited_set,word,index+1))

            visited_set.remove((i,j))
            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,visited_set,word,0):
                        return True
                        
        return False