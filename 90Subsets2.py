# Sort the array. Typical backtracking solution. To avoid duplicates if you selected a number before then skip it after the  pop.

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res = []
        nums.sort()
        def recur(i , curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            recur(i + 1, curr)
            curr.pop()
            while i < (len(nums) - 1) and nums[i+1] == nums[i]:
                i+=1
            recur(i + 1, curr)
            
        recur(0, [])
        return res
