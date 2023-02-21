class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp and index
        
        for idx, t in enumerate(temperatures):
            
            while stack and t > stack[-1][0]:
                topTemp, topIndex = stack.pop()
                res[topIndex] = idx - topIndex

            stack.append((temperatures[idx], idx))
            

        return res
