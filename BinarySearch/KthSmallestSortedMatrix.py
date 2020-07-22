from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        def count(num):
            cnt = 0
            i, j = n-1, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= num:
                    j += 1
                else:
                    cnt += j
                    i -= 1
            if i >= 0:
                cnt += j * (i+1)
            return cnt
        
        l, r = matrix[0][0], matrix[n-1][n-1]

        while l < r:
            mid = (l + r) // 2
            if count(mid) < k:
                l = mid+1
            else:
                r = mid

        return l


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8