# Binary Search for Insertion 
# T : O(NLOGN) for insertion and O(1) for finding Median

class MedianFinder:

    def __init__(self):
        self.nums= []

    def addNum(self, num: int) -> None:
        if len(self.nums) == 0:
            self.nums.append(num)

        else:
            index = self.search(num)
            if self.nums[index] < num:
                self.nums.insert(index + 1, num)
            else:
                self.nums.insert(index, num)

    def search(self, num):
        l, r = 0, len(self.nums) - 1

        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] == num:
                return mid
            elif self.nums[mid] > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return l

    def findMedian(self) -> float:
        size = len(self.nums)
        mid = size // 2
        return (self.nums[mid - 1] + self.nums[mid]) / 2 if size % 2 == 0 else self.nums[mid]
