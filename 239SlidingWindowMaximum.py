# Linear Time Algorithm
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # store indexs not values ( from nums )
        l = r = 0
        
        while r < len(nums):
            
            # pop the smaller values from the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            
            # pop the left val from the window
            if l > q[0]:
                q.popleft()
                
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        return output
            
        
