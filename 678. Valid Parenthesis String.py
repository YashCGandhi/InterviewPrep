class Solution:
    # Might have to mug it up. So, the premise is that if number of closing brackets > Maximum opening brackets possible then the answer is false.
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin -= 1
                leftMax += 1
            
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
            
        return leftMin == 0
