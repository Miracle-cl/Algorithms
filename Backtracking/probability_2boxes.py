import math
from typing import List

# problem id 1467
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        if not balls:
            return 0
        n_colors = len(balls)
        n = sum(balls) // 2
        box1 = [0] * n_colors
        box2 = [0] * n_colors
        box_cnt = [0, 0]
        prob = [0, 0]
        _mem = {}

        def factorial_m(n):
            if n in _mem:
                return _mem[n]
            _mem[n] = math.factorial(n)
            return _mem[n]

        def prod(arr):
            v = 1
            for x in arr:
                v *= factorial_m(x)
            return v


        prob[1] = factorial_m(2*n) // prod(balls)
        val_up = factorial_m(n) ** 2

        def dfs(color):
            if color >= n_colors:
                t1 = [x for x in box1 if x > 0]
                t2 = [x for x in box2 if x > 0]
                if len(t1) == len(t2):
                    prob[0] += val_up // (prod(t1) * prod(t2))
                    # print([box1, box2])
                return
            for c1 in range(balls[color]+1):
                c2 = balls[color] - c1
                if box_cnt[0]+c1 > n or box_cnt[1]+c2 > n:
                    continue
                box1[color] += c1
                box2[color] += c2
                box_cnt[0] += c1
                box_cnt[1] += c2
                dfs(color+1)
                box1[color] -= c1
                box2[color] -= c2
                box_cnt[0] -= c1
                box_cnt[1] -= c2

        dfs(0)
        return prob[0] / prob[1]


# balls = [1,2,2,1]
balls = [6,6,6,6,6,6]
# balls = [3,2,1]

ss = Solution()
res = ss.getProbability(balls)
print(res)