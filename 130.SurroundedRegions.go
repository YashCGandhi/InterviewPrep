func solve(board [][]byte)  {
    m, n := len(board), len(board[0])
    visit := make([][]bool, m)
    for i:=0;i<m;i++{
        visit[i] = make([]bool, n)
    }
    var dfs func(int, int)
    dfs = func(r int, c int){
        if r < 0 || r >= m || c < 0 || c >= n || visit[r][c] || board[r][c] != 'O'{
            return
        }
        visit[r][c] = true
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    }

    for i := 0; i < m; i++{
        dfs(i, 0)
        dfs(i, n - 1)
    }

    for j := 0; j < n;j++{
        dfs(0, j)
        dfs(m - 1, j)
    }

    for i:=0; i < m; i++{
        for j:=0; j < n; j++{
            if visit[i][j] == false{
                board[i][j] = 'X'
            }
        }
    }
}
