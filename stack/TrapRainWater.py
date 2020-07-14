from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # monotonic stack
        stack = []
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                topi = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                    ans += width * (min(h, height[stack[-1]]) - height[topi])
                    # print(ans)
            stack.append(i)
        return ans

    def trap_dp(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0

        left_max = height.copy()
        for i in range(1, length):
            left_max[i] = max(left_max[i], left_max[i-1])

        right_max = height.copy()
        for i in range(length-2, -1, -1):
            right_max[i] = max(right_max[i], right_max[i+1])

        ans = 0
        for i in range(length):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


# [0,1,0,2,1,0,1,3,2,1,2,1] -> 6