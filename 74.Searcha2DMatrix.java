class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        Integer ROWS,COLS;
        ROWS = matrix.length;
        COLS = matrix[0].length;

        int top = 0;
        int bot = ROWS - 1;
        int row = 0;

        while (top <= bot){
            row = (int) (top + bot ) / 2;
            if (matrix[row][0] > target){
                bot = row - 1;
            }else if(matrix[row][COLS-1] < target){
                top = row + 1;
            }
            else{
                break;
            }
        }

        int l = 0;
        int r = COLS - 1;
        int mid;
        while(l <= r){
            mid = (int)(l + r) / 2;
            if(matrix[row][mid] == target){
                return true;
            }
            else if(matrix[row][mid] > target){
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
        return false;

    }
}
