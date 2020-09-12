import bisect
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        l, r = 0, n-1
        while l < r and arr[l] <= arr[l+1]:
            l += 1

        while r >= l and arr[r-1] <= arr[r]:
            r -= 1

        # l == 0 and r == n-1 then 1
        # l > r then n
        if l > r:
            return 0 # max len is n
        if l == 0 and r == n-1:
            if arr[l] > arr[r]:
                return n - 1 # max len is 1
            else:
                return n - 2 # keep left and right
        
        if l == 0:
            # choose right side only (if - left)
            return r - (1 if arr[l] <= arr[r] else 0) # max len is n - r + (1)
        if r == n-1:
            # choose left side only (if + right)
            return n - l - 1 - (1 if arr[l] <= arr[r] else 0) # max len is l + 1 + (1)

        # 0< l < r < n-1
        def _find(l, r, m):
            # m is split of right side
            # find the split of left side to make max len
            left_len = bisect.bisect_right(arr, arr[m], lo=0, hi=l+1)
            return left_len

        ans = max(l + 1, n - r) # get left side or right side
        for m in range(r, n):
            ln = _find(l, r, m)
            ans = max(ans, ln + n - m)
        # print([ans])
        return n - ans


# arr = [1,2,3,10,4,2,3,5]
# arr = [5,4,3,2,1,2,3]
# arr = [6,11,20,20,7,22,22,22,6,4,9]
arr = [8,0,92,75,54,1,45,62,38,71,65,28,89,85,78,84,41,11,94,35,49,12,9,87,74,
53,48,43,92,77,66,49,27,11,8,81,60,66,6,63,63,37,27,62,82,60,42,64]
ss = Solution()
res = ss.findLengthOfShortestSubarray(arr)
print(res)