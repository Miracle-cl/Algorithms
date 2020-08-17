from typing import List

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        swap = [n] * n
        keep = [n] * n
        swap[0] = 1
        keep[0] = 0
        
        for i in range(1, n):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                swap[i] = swap[i-1] + 1
                keep[i] = keep[i-1]
            if A[i-1] < B[i] and B[i-1] < A[i]:
                swap[i] = min(keep[i-1] + 1, swap[i])
                keep[i] = min(swap[i-1], keep[i])
        # print(keep, swap)
        return min(keep[n-1], swap[n-1])


A = [1,3,5,4]
B = [1,2,3,7]
# A = [1,4,6,8]
# B = [3,2,3,4]
ss = Solution()
res = ss.minSwap(A, B)
print(res)