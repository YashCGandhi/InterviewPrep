# Recursive using LRU Cache. O(n) i guess
def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            # base case for odd length
            if i == j:
                return 1
            # base case for even length
            elif i > j:
                return 0
            
            if s[i] == s[j]:
                return 2 + dp(i+1,j-1)
            
            else:
                return max(dp(i + 1 , j), dp(i, j - 1))
            
        return dp(0, len(s) - 1)
      
 # 2-d Dp O(n^2)         
 def longestPalindromeSubseq(self, s: str) -> int:
        # Just like Longest Common Subsequence, the difference is that the two string are 's' and reverse of 's'
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        t = s[::-1]
        
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
                    
