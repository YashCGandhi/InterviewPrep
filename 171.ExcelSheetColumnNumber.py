# Hint use AB = A * 26^1 + B * 26^0

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #ZY 
        res= 0
        for j in range(len(columnTitle)-1,-1,-1):
            res += (ord(columnTitle[j]) - 64) * pow(26,len(columnTitle) -1 - j)
            
        return res
