class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        i = j = 0
        max_len = 2
        hashmap = {}

        while j < n:
            hashmap[s[j]] = j
            j += 1

            if len(hashmap) == 3:
                idx = min(hashmap.values())
                del hashmap[s[idx]]
                i = idx + 1
            max_len = max(max_len, j - i)
        return  max_len
