class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        else:
            target = target // 2

        sums = set()
        sums.add(0)
        
        for i in range(len(nums)):
            nextDP = set()
            for s in sums:
                if nums[i] + s == target:
                    return True
                nextDP.add(s)
                nextDP.add(nums[i] + s)
            sums = nextDP
        return False
            
