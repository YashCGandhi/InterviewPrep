class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(index, row, col):
            if index == len(word):
                    return True
            if min(row, col) < 0 or row >= ROWS or col >= COLS or (row, col) in path or board[row][col] != word[index]:
                return False
            path.add((row, col))
            res = (
                backtrack(index + 1, row + 1, col)
                or backtrack(index + 1, row, col + 1)
                or backtrack(index + 1, row - 1, col)
                or backtrack(index + 1, row, col - 1) 
            )
            path.remove((row, col))
            return res


        # To avoid TLE check if the first char is more frequent than the last char in the word. If so reverse the word.
        count = Counter(word)
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0, r, c):
                    return True
        return False


        
