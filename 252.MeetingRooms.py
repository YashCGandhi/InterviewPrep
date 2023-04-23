class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort()
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if start < prevEnd:
                return False
            else:
                prevEnd = end
        
        return True
