class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        n, m = len(s), len(t)
        # make sure the first string is smaller than the second one
        if n > m :
            return self.isOneEditDistance(t,s)
        # if the differnce is > than 1 then is False by default
        if m - n > 1:
            return False

        for i in range(n):
            if s[i] != t[i]:
                if n == m:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        # the string match until one is  over, the second string should have one more element.
        return n + 1 == m
