class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posD = set()
        negD = set()
        board = [["." for _ in range(n)] for _ in range(n)]
        
        
        def backtrack(index):
            if index == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for i in range(n):
                if i in col or (index + i) in posD or (index - i) in negD:
                    continue

                col.add(i)
                posD.add(index + i)
                negD.add(index - i)
                board[index][i] = 'Q'

                backtrack(index + 1)

                col.remove(i)
                posD.remove(index + i)
                negD.remove(index - i)
                board[index][i] = "."
        backtrack(0)
        return res
