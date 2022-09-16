# N^2 Time Limit Exceeded ( Top Down DP )
def jump(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        
        def helper(A, start):
            if start >= len(A) - 1:
                return 0
            if dp[start]:
                return dp[start]
            
            minJump = float("inf")
            for i in range(start + 1, start + A[start] + 1):
                minJump = min(minJump, 1 + helper(A, i))
            dp[start] = minJump
            return dp[start] 
        
        return helper(nums, 0)
      
# Greedy Solution
def jump(self, nums: List[int]) -> int:
        # This is a greedy solution, the idea is that we find out the farthest element which can be reached from a window of elements i.e L to R. For example, 2,3,1,1,4 .. initally the window is L = R = 0 that means that the 0th element is in the window and the farthest we can go from there is the 2nd position. Now, the L and R will be updated as L = R + 1 and R = farthest position. Now, we go again finding the farthest from the new L and R. And once the R goes >= len(nums) - 1 we return. As, we have to return minJumps required, the way we find that out is we add a variable 'res' initialized to 0. This res will be updated everytime we change the L and R values i.e everytime we jump we change the res to res + 1. 
        res = 0
        l = r = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
