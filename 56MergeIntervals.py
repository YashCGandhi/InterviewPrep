def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = merged[-1][1]
            
            if start <= lastEnd :
                merged[-1][1] = max(end,lastEnd)
            else:
                merged.append([start,end])
        return merged
