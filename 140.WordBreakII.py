"""
This was initially a recursive solution.
we start from the begginning and check if any word matches the start of the string ( or sometimes the whole string).
Then the subproblem is checking if any word matches the s[len(previousMatch) : ] and so on.

dp is introducted to avoid repeating the calculating of the same string again and again.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        def helper(s):
            if s in dp: return dp[s]
            result = []

            for w in wordDict:
                if s[:len(w)] == w:
                    if len(w) == len(s):
                        result.append(w)
                    else:
                        tmp = helper(s[len(w):])
                        for t in tmp:
                            result.append(w + " " + t)
            dp[s] = result
            return result

        return helper(s) 
