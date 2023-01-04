class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # T: O(N)
        # S: O(N)
        # hashset = {}
        # for n in nums:
        #     hashset[n] = 1
        # max_ele = len(nums) + 1

        # for i in range(1,max_ele + 1):
        #     if i not in hashset:
        #         return i


        # T: O(N)
        # S: O(1)
        
        for i, v in enumerate(nums):
            if v < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        return len(nums) + 1
