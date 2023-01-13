# T : O(N^2)
class Solution:
    def findCelebrity(self, n: int) -> int:
        not_celeb = set()
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i in not_celeb:
                    break
                elif i != j:
                    if not knows(i,j) and knows(j,i):
                        not_celeb.add(j)
                        cnt += 1
                    else:
                        not_celeb.add(i)
                        break
            if cnt == n - 1:
                return i
        return -1  
