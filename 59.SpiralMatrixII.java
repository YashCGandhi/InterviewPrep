class Solution {
    public int[][] generateMatrix(int n) {
        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;
        int cnt = 1;
        int[][] result = new int[n][n];

        while (bottom >= top && right >= left){
            for (int i = left; i <= right; i++){
                result[top][i] = cnt;
                cnt++;
            }
            top++;

            for (int i = top; i <= bottom; i++){
                result[i][right] = cnt;
                cnt++;
            }
            right--;

            for (int i = right; i >= left; i--){
                result[bottom][i] = cnt;
                cnt++;
            }
            bottom--;

            for (int i = bottom; i >= top; i--){
                result[i][left] = cnt;
                cnt++;
            }
            left++;
        }

        return result;
    }
}
