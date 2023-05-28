class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1){
                    int cnt = helper(grid, i, j);
                    res = max(res, cnt);
                }
            }
        }

        return res;
    }

    private int max(int a, int b){
        if (a > b){
            return a;
        }
        return b;
    }

    private int helper(int[][] grid, int i, int j){
        if (i < 0 || i >= grid.length || j < 0  || j >= grid[0].length || grid[i][j] == 0){
            return 0;
        }
        grid[i][j] = 0;
        return (1 + helper(grid, i - 1,j) + helper(grid, i + 1, j) + helper(grid, i , j - 1) + helper(grid, i , j + 1));
    }
}
