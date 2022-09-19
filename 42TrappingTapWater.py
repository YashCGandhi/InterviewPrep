# Create LeftMax and RightMax arrays and use them to calculate the trapped rain water at an index.
# Time Complexity O(n) and Space Complexity O(n).
def trap(self, height: List[int]) -> int:
        
        area = 0
        left_max = [0 for i in range(len(height))]
        right_max = [0 for i in range(len(height))]
        
        right_max[len(height) - 1] = height[len(height) - 1]
        
        for i in range(0,len(height)):
            left_max[i] = max(left_max[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
        
        for i,h in enumerate(height):
            if height[i] < min(left_max[i], right_max[i]):
                area += min(left_max[i], right_max[i]) - height[i]
        
        return area


# Two pointer method, use the min of Current LeftMax and RightMax to calculate the rain water to be stored. 
# Time Complexity O(n) and Space Complexity O(1).
def trap(self, height: List[int]) -> int:
        
     
        
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
