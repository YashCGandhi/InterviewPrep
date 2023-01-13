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
 
        # T : O(n)
        # As there is only one celebrity in a party, keep updating the candidate in the following manner, it will lead to the celeb if they exisit .
        candidate = 0
        for i in range(1,n):
            if knows(candidate, i):
                candidate = i
        
        for i in range(n):
            if i != candidate and (knows(candidate,i) or not knows(i, candidate)):
                return -1
        return candidate
