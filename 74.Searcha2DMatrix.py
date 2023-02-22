class Solution:
    def binarySearch(self, row, target):
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return mid
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return - 1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        r = 0
        while r < ROWS:
            if target <= matrix[r][COLS-1]:
                index = self.binarySearch(matrix[r], target)
                return True if index != -1 else False
            r += 1

