"""
Split the string into substring if you come accross a char that occurs < k times in string. Then run the same algorithm on both the parts to check for max len.
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n < k:
            return 0
        
        if k <= 1:
            return n

        counts = Counter(s)

        l = 0
        while l < n and counts[s[l]] >= k:
            l += 1
        if l >= n - 1:
            return l
        
        ls1 = self.longestSubstring(s[:l], k)
        while l < n and counts[s[l]] < k:
            l += 1
        ls2 = self.longestSubstring(s[l:],k) if l < n else 0

        return max(ls1, ls2)
