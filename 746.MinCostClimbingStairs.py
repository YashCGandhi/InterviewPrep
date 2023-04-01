class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost[0], cost[1])
        minCostArray = [0] * (len(cost))
        minCostArray[-1] = cost[-1]
        minCostArray[-2] = cost[-2]
        
        for i in range(len(minCostArray)-3, -1, -1):
            minCostArray[i] = min(cost[i] + minCostArray[i+1], cost[i] + minCostArray[i+2])
            
        return min(minCostArray[0], minCostArray[1])
