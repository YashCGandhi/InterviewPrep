class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        cur = []
        
        def backtrack(index):
            if index == len(s):
                res.append(cur.copy())
                return
            for i in range(index,len(s)):
                if self.isPali(s, index, i):
                    cur.append(s[index:i+1])
                    backtrack(i+1)
                    cur.pop()

        backtrack(0)
        return res
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
