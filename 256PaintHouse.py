class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # cost[i][j] i is house, j is color.
        
        dp = [0, 0, 0]
        
        for n in range(len(costs)):
            dp0 = costs[n][0] + min(dp[1], dp[2])
            dp1 = costs[n][1] + min(dp[0], dp[2])
            dp2 = costs[n][2] + min(dp[0],dp[1])
            
            dp = [dp0, dp1, dp2]
            
        return min(dp)
