def trap(self, height: List[int]) -> int:
        
        # Two pointer method, use the min of Current LeftMax and RightMax to calculate the rain water to be stored.
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        if not height: return 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                minHeight = min(leftMax, rightMax)
                if minHeight - height[l] > 0:
                    res += minHeight - height[l]
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                minHeight = min(leftMax, rightMax)
                if minHeight - height[r] > 0:
                    res += minHeight - height[r]
                rightMax = max(rightMax, height[r])
        return res
      
