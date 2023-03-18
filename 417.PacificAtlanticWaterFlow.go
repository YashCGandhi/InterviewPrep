func pacificAtlantic(heights [][]int) [][]int {
    ROWS, COLS := len(heights), len(heights[0])
    res := [][]int{}

    pac, atl := make([][]bool, ROWS), make([][]bool, ROWS)
    for r := 0; r < ROWS; r++{
        pac[r] = make([]bool, COLS)
        atl[r] = make([]bool, COLS)
    }

    var dfs func(int, int, [][]bool, int)

    dfs = func(r int, c int, visit [][]bool, prevHeight int){
        if r < 0 || c < 0 || r == ROWS || c == COLS || heights[r][c] < prevHeight || visit[r][c]{
            return 
        }
        visit[r][c] = true
        dfs( r + 1, c, visit, heights[r][c])
        dfs( r - 1, c, visit, heights[r][c])
        dfs( r, c + 1, visit, heights[r][c])
        dfs( r, c - 1, visit, heights[r][c])
    }

    for c := 0; c < COLS; c++{
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
    }

    for r := 0; r < ROWS; r++{
        dfs( r, 0, pac, heights[r][0])
        dfs( r, COLS - 1, atl, heights[r][COLS - 1])
    }

    for i := 0; i < ROWS; i++{
        for j := 0; j < COLS; j++{
            if pac[i][j] && atl[i][j]{
                res = append(res, []int{i, j})
            }
        }
    }

    return res
}
