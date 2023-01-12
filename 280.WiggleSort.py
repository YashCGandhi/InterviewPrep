class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # Sort the nums array and make sure every even index follows nums[i] < nums[i+1] and for every odd index nums[i] > nums[i+1]
        # T : O(NlogN)
        # S : O(1)
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1],nums[i]
            elif i % 2 == 1:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1],nums[i]
            i += 1
        print(nums)
