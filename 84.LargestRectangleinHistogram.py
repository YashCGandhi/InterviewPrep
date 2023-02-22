class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        N = len(heights)
        max_height = 0

        for i in range(len(heights)):
            if not stack:
                stack.append((i, heights[i]))
                continue

            if stack[-1][1] < heights[i]:
                stack.append((i, heights[i]))
                continue

            if stack[-1][1] > heights[i]:            
                while stack and stack[-1][1] > heights[i]:
                    idx = stack[-1][0]
                    max_height = max(max_height, (i - stack[-1][0]) * stack[-1][1])
                    stack.pop()
                stack.append((idx, heights[i]))

        while stack:
            idx, height = stack.pop()
            max_height = max(max_height, (N - idx) * height)

        return max_height



