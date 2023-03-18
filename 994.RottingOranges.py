class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0,0
        # 1,0 - 
        m, n = len(grid), len(grid[0])
        q = deque([])
        DIR = [0,1,0,-1,0]
        count = 0
        mx = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    count += 1
        if count == 0:
            return 0
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                mx = max(mx, grid[nr][nc])
                count -= 1
                q.append((nr,nc))
            
        if count > 0 :
            return -1
        return mx - 2
