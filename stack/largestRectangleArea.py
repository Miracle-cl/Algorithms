from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        i = max_area = 0
        size = len(heights)
        while i < size:
            h = heights[i]
            if not stack or heights[stack[-1]] < h:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                max_area = max(max_area,
                               heights[top] * (i - stack[-1] - 1 if stack else i))
        while stack:
            top = stack.pop()
            max_area = max(max_area,
                           heights[top] * (i - stack[-1] - 1 if stack else i))
        return max_area

    def largestRectangleArea1(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        i = 0
        while (i < len(heights)):
            if (not stack) or (heights[i] > heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                tmp = stack.pop()
                max_area = max(max_area,
                               heights[tmp] * ((i - stack[-1] - 1) if stack else i))
        return max_area

s = Solution()
h = [2,1,5,6,2,3]
print(s.largestRectangleArea1(h))
