# My Code-Solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        "Hint : find the O's that will not be flipped"
        m, n = len(board), len(board[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visit or board[r][c] != "O":
                return

            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        
        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visit:
                    board[i][j] = "X"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        # Find out all the 'O's that are not surrounded and switch them to 'T' 
        def capture(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != 'O':
                return
            board[r][c] = "T"
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            for d in range(len(dirs)):
                capture(r+dirs[d][0], c + dirs[d][1])
            
        
        # DFS ('O'->'T') 
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' and (r in [0,ROWS-1] or c in [0, COLS-1])):
                    capture(r, c)

        # Convert all the surrounded 'O's to 'X's
        # 'O' -> 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        #  'T' -> 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
