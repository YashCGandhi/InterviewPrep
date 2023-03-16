func maxAreaOfIsland(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    res := 0

    for i := 0; i < m; i++{
        for j := 0; j < n; j++{
            if grid[i][j] == 1{
                cnt := dfs(grid, i, j)
                if cnt > res{
                    res = cnt
                }
            }
        }
    }
    
    return res
}

func dfs(grid [][]int, r ,c int) int {
    if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) || grid[r][c] != 1{
        return 0
    }

    grid[r][c] = 0
    return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)
} 
