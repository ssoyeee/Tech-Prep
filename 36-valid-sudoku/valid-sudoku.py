class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        cols = defaultdict(set) # key => col num, val => set
        rows = defaultdict(set) # key => row num, val => set
        squares = defaultdict(set) # 3*3  
        # (0,0): {"5", "3", "6"}, 
        # (1,1): {"8"},

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".": 
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c]) 
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
    # Time O(1), O(N^2) N=9 O(81)
    # Space O(1), O(3N) O(3*9)=O(27)
