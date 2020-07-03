from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) < 2:
            return len(A)
        anchor = 0
        ans = 1
        length = len(A)
        def cmp(a, b):
            if a < b:
                return 1
            if a == b:
                return 0
            return -1

        for i in range(1, length):
            c = cmp(A[i-1], A[i])
            if c == 0:
                anchor = i
            elif i+1 < length and c * cmp(A[i], A[i+1]) > -1:
                ans = max(ans, i-anchor+1)
                anchor = i
        ans = max(ans, i-anchor+1)
        return ans

    def maxTurbulenceSize_1(self, A: List[int]) -> int:
        anchor = 0
        ans = 1
        length = len(A)
        def cmp(a, b):
            if a < b:
                return 1
            if a == b:
                return 0
            return -1

        for i in range(1, length):
            c = cmp(A[i-1], A[i])
            if c == 0:
                anchor = i
            elif i+1 == length or c * cmp(A[i], A[i+1]) > -1:
                ans = max(ans, i-anchor+1)
                anchor = i
        # ans = max(ans, i-anchor+1)
        return ans


# A = [9,4,2,10,7,8,2,4,3]
# A = [9,4,2,10,7,8,8,1,9]