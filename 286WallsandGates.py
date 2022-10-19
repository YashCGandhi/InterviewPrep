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
        
                    
