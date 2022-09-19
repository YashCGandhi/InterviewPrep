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
