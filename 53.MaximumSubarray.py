class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy mind being, " if the sum isn't positive its useless "
        curSum = nums[0]
        res = curSum
        for i in range(1, len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            res = max(res, curSum)
        
        return res
