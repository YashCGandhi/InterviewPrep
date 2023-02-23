# Initail Solution

class TimeMap:

    def __init__(self):
        self.records = [] # (time stamp, {key:value})

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.records.append((timestamp, {key:value}))
        
    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.records) - 1
        while l < r:
            mid = (l + r) // 2
            if self.records[mid][0] == timestamp:
                return self.records[mid][1][key]
            elif self.records[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        for i in range(l, -1, -1):
            if self.records[i][0] <= timestamp and key in self.records[i][1].keys():
                return self.records[i][1][key]
        
        return "" 
 
