func numIslands(grid [][]byte) int {
    m, n := len(grid), len(grid[0])
    count := 0

    var dfs func(i int, j int)
    dfs = func(i int, j int){
        if i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0'{
            return
        }
        grid[i][j] = '0'

        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)
    }

    for i, row := range grid{
        
        for j, point := range row {
            
            if point == '1'{
                count++
                dfs(i, j)
            }
        }
    }
    return count
}
