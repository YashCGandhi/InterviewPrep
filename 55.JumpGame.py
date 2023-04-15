class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # This is a greedy solution. So, let the last index be the goal we need to reach. start the loop in reverse from the second last index and check if you can reach the current goal. If you can, then shift the goal to the index you are currently on. And if the goal is 0 by the end of the loop then return True else False.
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0

        # This one is O(N^2) solution. DP Memo solution.
        # dp = [False] * len(nums)
        # dp[-1] = True

        # for i in range(len(nums) - 1, -1, -1):
        #     if dp[i]:
        #         continue
        #     for j in range(i + 1, min(len(nums), i + nums[i]) + 1):
        #         if dp[j]:
        #             dp[i] = True
        #             break
        # return dp[0]
