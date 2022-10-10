class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        
        self.q = collections.deque()
        self.sum = 0
        self.count = 0
    def next(self, val: int) -> float:
        
        self.count += 1
        
        self.q.append(val)
        tail = self.q.popleft() if self.count > self.size else 0
        
        self.sum += val - tail
        
        return self.sum / min(self.size, self.count)
