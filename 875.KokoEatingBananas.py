class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        totalTime = max(piles)
        while l <= r:
            k = (l + r) // 2
            cnt = 0
            for i in range(len(piles)):
                cnt += math.ceil(piles[i] / k)
            if cnt > h:
                l = k + 1
            else:
                totalTime = min(totalTime, k)
                r = k - 1
        return totalTime
    
