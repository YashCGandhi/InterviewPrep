# T : O(N^2)
class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calender:
            if s < end and start < e:
                return False
        self.calender.append((start,end))
        return True


# Binary Search - O(LogN) insertions

class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        
        l, r = 0, len(self.calender)

        if r == 0:
            self.calender.append((start, end))
            return True
        while l < r:
            mid = (l + r) // 2
            if self.calender[mid][1] <= start:
                l = mid + 1
            else:
                r = mid

        if l == len(self.calender):
            self.calender.append((start,end))
            return True
        if self.calender[l][0] >= end:
            self.calender.insert(l,(start, end))
            return True

        return False
        



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
