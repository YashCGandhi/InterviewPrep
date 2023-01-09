class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Strip consecutive '*'s
        newP = ''
        for i in range(len(p)):
            if p[i] != '*' or i == 0 or p[i-1] != '*':
                newP += p[i]
        p = newP

        len_s, len_p = len(s), len(p)

        dp = [[False for i in range(len_p + 1)] for j in range(len_s + 1)]

        dp[0][0] = True

        # populate the zeroth row and col.Checking for '*' as first char
        for j in range(len(p)):
            if p[j] != '*':
                # A letter or ? won't match the empty string.
                dp[0][j+1] = False
            else:
                # If star, take the previous entry.
                dp[0][j+1] = dp[0][j]
        for i in range(len(s)):
            #The empty pattern doesn't match any characters
            dp[i+1][0] = False

        for j in range(len_p):
            for i in range(len_s):
                if p[j] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
                elif p[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i][j] and p[j] == s[i]

        return dp[len_s][len_p]
