def isRobotBounded(self, instructions: str) -> bool:
        # IF the robot ends up back at origin or the direction has changed then, the robot is in a circle
        dirX, dirY = 0, 1
        x = y = 0
        
        for i in instructions:
            if i == 'G':
                x, y = x + dirX, y + dirY
            elif i == 'L':
                dirX, dirY = -1*dirY, dirX
            else:
                dirX, dirY = dirY, -1*dirX
        
        if (x == 0 and y == 0) or dirX != 0 or dirY != 1:
            return True
        else: 
            return False
