class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 1, x // 2
        mid = (l + r) // 2
        while l <= r:
            mid = (l + r) // 2
            num = mid * mid
            if num < x:
                l = mid + 1
            elif num > x:
                r = mid - 1
            else:
                return mid
        return r
                
            
            
        
        
