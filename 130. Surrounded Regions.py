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
