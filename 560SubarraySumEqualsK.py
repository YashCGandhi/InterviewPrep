# The numbers in the array given are not sorted and could be between -1000 to 1000. So, a sliding window technique does not work as there is no telling if the next value   is greater or smaller than the previous one and how it would affect the current sum. Then, we calculate prefix Sums. Every time we calculate a new curSum we add it to   the hashmap so that we know that we have a prefix which has a value of x and which can be removed to get a desired Sum.

def subarraySum(self, nums: List[int], k: int) -> int:
        res, curSum = 0, 0
        prefixSum = {0:1}
        for v in nums:
            curSum += v
            diff = curSum - k
            
            
            res += prefixSum.get(diff, 0)
            
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res
