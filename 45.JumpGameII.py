class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res  

        # jumps = [float("inf")] * len(nums)

        # jumps[-1] = 0

        # for i in range(len(nums)- 2, -1, -1):
        #     minJumps = float("inf")
        #     for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
        #         minJumps = min(minJumps, jumps[j])
        #     jumps[i] = 1 + minJumps
        
        # return jumps[0]
