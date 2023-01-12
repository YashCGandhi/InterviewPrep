class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # sort the nums, and then assign the even indexs with the first half of the sorted array reversed and assign the odd indexes the second part of the sorted array reversed.
        # Note that the arrays are reversed because we cannot have nums[i] == nums[i+1] as this case might come up if the second half is directly placed in the odd indexes.
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        
