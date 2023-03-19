## My Solution
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        visit = set()
        dirs = [[1,0],[-1,0],[0,-1],[0,1]]
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))
        
        while q:
            l = len(q)
            for i in range(l):
                x, y = q.popleft()
                for d in dirs:
                    new_x, new_y = x + d[0], y + d[1]
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or rooms[new_x][new_y] == -1 or (new_x, new_y) in visit:
                        continue
                    visit.add((new_x, new_y))
                    rooms[new_x][new_y] = rooms[x][y] + 1
                    q.append((new_x, new_y))
            


## My Solution Ends
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        r, c = len(rooms), len(rooms[0])
        q = deque()
        visited = set()
        directions = [[1,0], [0, -1], [-1,0], [0,1]]
        
        def addRoom(m, n):
            if m == r or m < 0 or n == c or n < 0 or rooms[m][n] == -1 or (m, n) in visited:
                return 
            visited.add((m, n))
            q.append([m, n])
        
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    visited.add((i,j))
                    
        dist = 0
        while q:
            for i in range(len(q)):
                curRow, curCol = q.popleft()
                rooms[curRow][curCol] = dist
                
                addRoom(curRow + 1, curCol)
                addRoom(curRow - 1, curCol)
                addRoom(curRow, curCol + 1)
                addRoom(curRow, curCol - 1)
            dist += 1
        
                    
