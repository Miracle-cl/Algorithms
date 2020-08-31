from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        _f = {}
        # f(l, r, k): max scores remove boxes [l, l+1, ... r], and there are k boxes same as boxes[r]
        # <==>  seqs: [a[l], a[l+1], a[r]] + {x1, x2, .. xk}; (xi == a[r]) 
        def f(l, r, k):
            if l > r:
                return 0
            if (l, r, k) in _f:
                return _f[l, r, k]
            while r > l and boxes[r-1] == boxes[r]:
                r -= 1
                k += 1
            ans = f(l, r-1, 0) + (k+1)*(k+1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    ans = max(ans, f(l, i, k+1) + f(i+1, r-1, 0))
            _f[l, r, k] = ans
            return ans

        return f(0, n-1, 0)


if __name__ == '__main__':
    boxes = [1,3,2,2,2,3,4,3,1]
    # boxes = [6,3,6,5,6,7,6,6,8,6]
    ss = Solution()
    res = ss.removeBoxes(boxes)
    print(res)