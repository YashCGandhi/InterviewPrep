class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        #copy = [[board[r][c] for c in range(COLS)] for r in range(ROWS)]
        def get_live_cells(r, c):
            dirs = [[0,1],[1,1], [1,0],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
            live = 0
            for d in dirs:
                if r + d[0] >= 0 and r + d[0] < ROWS and c + d[1] >= 0 and c + d[1] < COLS:
                    # check copy[r+d[0]][c + d[1]] == 1 for Space Complexity O(mn)
                    if abs(board[r + d[0]][c + d[1]]) == 1:
                        live += 1
            return live 
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         live = get_live_cells(r, c)
        #         if copy[r][c] == 1 and (live < 2 or live > 3):
        #             board[r][c] = 0
                
        #         if copy[r][c] == 0 and live  == 3:
        #             board[r][c] = 1

        for r in range(ROWS):
            for c in range(COLS):
                live = get_live_cells(r, c)
                if board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = -1
                
                if board[r][c] == 0 and live == 3:
                    board[r][c] = 2
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] > 0:

                    board[r][c] = 1
                else:

                    board[r][c] = 0
                
