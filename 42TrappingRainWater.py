#O(n) Time and O(n) Space
# Water at Anypoint can be calcuted as min(Lmax, Rmax) - height[i]
# Calculate the Lmax array and the Rmax array then its a piece of cake.
def trap(self, height: List[int]) -> int:
        L, R = [0] * (len(height)), [0]* (len(height))
        res = 0
        for i in range(1,len(height)):
            
            L[i] = max(L[i-1],height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            R[i] = max(R[i+1],height[i+1])
            
        
        for i in range(len(height)):
            water = min(L[i],R[i]) - height[i]
            if water > 0:
                res += water
        
        return res








# O(n) Time and O(1) Space.
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
      
