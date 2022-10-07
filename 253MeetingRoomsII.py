

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        
        s = e = 0
        rooms, available =0, 0
        
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
            
        start.sort()
        end.sort()
        
        while s < len(start):
            if start[s] < end[e]:
                if available > 0:
                    available -= 1
                    
                else:
                    rooms += 1
                s += 1
            else:
                available += 1
                e += 1
        return rooms
