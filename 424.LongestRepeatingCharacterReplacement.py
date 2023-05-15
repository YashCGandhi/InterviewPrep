class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        res = 0
        r = 0
        while r < len(s):
            d[s[r]] = 1 + d.get(s[r], 0)

            while (r - l + 1) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) 
            r += 1
            
        return res


        
