class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.dirs = {'R':[0,1], 'L':[0,-1], 'U':[-1,0],'D':[1,0]}
        self.snake = [[0,0]]
        self.l = 0
        self.f = 0
    def move(self, direction: str) -> int:
        # if curr_loc + direction == food:
            # increase len by 1 and head is at the foods location
        # else add the next direction to the curr_loc and pop the last element fromt the queue.
        # if the head is out of bounds or head is in the snake array then return -1
        x,y = self.snake[-1]
        next_x, next_y = self.dirs[direction]
        curr_x, curr_y = x + next_x, y + next_y
        if self.f < len(self.food) and curr_x == self.food[self.f][0] and curr_y == self.food[self.f][1]:
            self.snake.append([curr_x, curr_y])
            self.l += 1
            self.f += 1
        
        elif curr_x < 0 or curr_x >= self.height or curr_y < 0 or curr_y >= self.width or [curr_x,curr_y] in self.snake[1:]:
            return -1
        else:
            self.snake.append([curr_x, curr_y])
            del self.snake[0]
        
        return self.l
        



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
