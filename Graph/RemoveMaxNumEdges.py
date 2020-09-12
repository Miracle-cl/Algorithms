from typing import List
import copy


class DJS:
    # disjoint set
    def __init__(self, n):
        self.root = list(range(1+n))

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def merge(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return 0
        self.root[px] = py
        return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        d3 = DJS(n)
        e_cnt = 0
        # merge type 3 edge
        for ti, u, v in edges:
            if ti != 3:
                continue
            if d3.merge(u, v):
                e_cnt += 1
            
        if e_cnt == n-1:
            return len(edges) - e_cnt

        # merge type 1 edge to e_cnt == n-1
        d1 = copy.deepcopy(d3)
        a_cnt = 0
        for ti, u, v in edges:
            if ti != 1:
                continue
            if d1.merge(u, v):
                a_cnt += 1
            if a_cnt + e_cnt == n-1:
                break
        if a_cnt + e_cnt < n-1:
            return -1
        
        # merge type 2 edge to e_cnt == n-1
        d2 = copy.deepcopy(d3)
        b_cnt = 0
        for ti, u, v in edges:
            if ti != 2:
                continue
            if d2.merge(u, v):
                b_cnt += 1
            if b_cnt + e_cnt == n-1:
                break
        if b_cnt + e_cnt < n-1:
            return -1
            
        return len(edges) - e_cnt - a_cnt - b_cnt



n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]

ss = Solution()
res = ss.maxNumEdgesToRemove(n, edges)
print(res)