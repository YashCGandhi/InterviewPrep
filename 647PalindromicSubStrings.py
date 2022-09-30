def countSubstrings(self, s: str) -> int:
        # iterate through the string 's' and assume 'i' as a middle point of a palindrome. Then, keep going left and right untill s[l] != s[r] and keep adding the palindromes to the result. for Odd length string l = r = i and for even length strings l = i and r = i + 1
    
    # O(n^2) time complexity.
        res = 0
        for i in range(len(s)):

            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
                    
        return res
