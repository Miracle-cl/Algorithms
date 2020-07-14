from typing import List
from collections import deque


class FenwickTree:
    def __init__(self, n):
        self._sums = [0 for _ in range(n + 1)]
        
    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & -i
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & -i
        return s


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        lens = len(num)
        if k >= lens * (lens-1) / 2:
            return ''.join(sorted(num))

        used = [0] * lens
        position = [deque() for _ in range(10)]
        for i, n in enumerate(num):
            position[int(n)].append(i)

        ft = FenwickTree(lens)
        res = ''
        while k > 0 and len(res) < lens:
            for i in range(10):
                if not position[i]:
                    continue
                top = position[i][0] # cannot pop here
                cost = top - ft.query(top) # top , top+1, not same index
                if cost > k:
                    continue
                k -= cost
                ft.update(top+1, 1)
                used[top] = 1
                res += num[top]
                position[i].popleft()
                break # updata one character to res then break and new cycle
                
        for i in range(lens):
            if not used[i]:
                res += num[i]
        return res


if __name__ == '__main__':
    # num = "294984148179"
    # k = 11
    num = '3142'
    k = 4
    ss = Solution()
    res = ss.minInteger(num, k)
    print(res)