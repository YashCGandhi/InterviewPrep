class Solution:
  # My solution - O(n) space and O(n) Time
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) < 4:
    #         return max(nums)

    #     def houserobber(money):
    #         dp = [0] * len(money)
    #         dp[0] = money[0]
    #         dp[1] = max(money[0], money[1])

    #         for i in range(2, len(money)):
    #             dp[i] = max(money[i] + dp[i - 2], dp[i - 1])
    #         return dp[-1]
        
    #     return max(houserobber(nums[:-1]),houserobber(nums[1:]))

    # Space - O(1) and Time - O(n)
    def rob(self, nums):

        def houserobber(money):
            rob1,  rob2 = 0, 0

            for m in money:
                newRob = max(rob1 + m, rob2)
                rob1 = rob2
                rob2 = newRob

            return rob2

        return max(nums[0], houserobber(nums[1:]), houserobber(nums[:-1]))  
