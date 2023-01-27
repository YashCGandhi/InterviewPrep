class HitCounter:

    def __init__(self):
        self.ts = deque([])

    def hit(self, timestamp: int) -> None:
        self.ts.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while len(self.ts) > 0 and self.ts[0] + 300 <= timestamp:
            self.ts.popleft()
        return len(self.ts)
        
