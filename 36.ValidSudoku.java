class Solution {
    public boolean isValidSudoku(char[][] board) {
        int rows = board.length;
        int cols = board[0].length;
        
        Set<Character> rowSet = null;
        Set<Character> colSet = null;

        // check rows
        for (int r = 0; r < rows; r++){
            rowSet = new HashSet<>();
            for (int c = 0; c < cols; c++){
                if (board[r][c] == '.'){
                    continue;
                }else{
                    if (rowSet.contains(board[r][c])){
                        return false;
                    }else{
                        rowSet.add(board[r][c]);
                    }
                }
            }
        }

        // check cols
        for (int c = 0; c < cols; c++){
            colSet = new HashSet<>();
            for (int r = 0; r < rows; r++){
                if (board[r][c] == '.'){
                    continue;
                }else{
                    if (colSet.contains(board[r][c])){
                        return false;
                    }else{
                        colSet.add(board[r][c]);
                    }
                }
            }
        }

        // check squares
        for (int r = 0; r < rows; r = r + 3){
            for (int c = 0; c < cols; c = c + 3){
                
                if (!checkSquare(r, c, board)){
                    return false;
                }
            }
        }

        return true;

    }
    public boolean checkSquare(int i, int j, char[][] board){
        Set<Character> squareSet = new HashSet<>();
        for (int r = i; r < i + 3; r++){
            for (int c = j; c < j + 3; c++){
                
                if (board[r][c] == '.'){
                    continue;
                }else{
                    if(squareSet.contains(board[r][c])){
                        return false;
                    }else{
                        squareSet.add(board[r][c]);
                    }
                
                }
            }
        }
        return true;
    }
}
