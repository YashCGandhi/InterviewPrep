class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        hashmap = {}
        max_len = 0
        i = j = 0
        while j < len(s):
            hashmap[s[j]] = j
            if len(hashmap) == k + 1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                i = del_idx + 1
            
            max_len = max(max_len, j - i + 1)
            j += 1
        
        return max_len
