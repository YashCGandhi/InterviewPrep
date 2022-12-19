class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]^nums[j] == 0:
        #             return nums[i]

        slow, fast = 0, 0
        while True:
            slow=nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow1 = 0
        while True:
            slow1 = nums[slow1]
            slow = nums[slow]

            if slow1 == slow:
                break
        
        return slow
