class HitCounter:

    def __init__(self):
        self.ts = []

    def hit(self, timestamp: int) -> None:
        self.ts.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        hits = 0
        for i in range(len(self.ts) - 1,-1, -1):
            if -300 < self.ts[i] - timestamp <= 0:
                hits += 1
        return hits
        
