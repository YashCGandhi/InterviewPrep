class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        res = []

        def backtrack(i, dots, curIP):

            if dots == 4 and i == size:
                res.append(curIP[:-1])
                return

            if dots > 4:
                return 
            
            for j in range(i, min(i + 3, size)):
                if int(s[i:j+1]) < 256 and (len(s[i:j+1]) == 1 or s[i] != '0'):
                    backtrack( j+1, dots + 1, curIP + s[i:j+1] + '.')

        backtrack(0, 0 , "")    
        return res
