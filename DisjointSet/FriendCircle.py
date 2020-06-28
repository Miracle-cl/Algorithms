from typing import List


class UnionFindSet:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.ranks = [0] * n
        
    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        elif self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True
    
    
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        ufs = UnionFindSet(n)
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    ufs.union(i, j)
        
        circles = set()
        for i in range(n):
            circles.add(ufs.find(i))
        return len(circles)

    def findCircleNum_dfs(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        cnt = 0
        visited = set()
        
        def dfs(i):
            for j in range(n):
                if j in visited or M[i][j] == 0:
                    continue
                visited.add(j)
                dfs(j)
                    
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            cnt += 1
        return cnt


M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
ss = Solution()
res1 = ss.findCircleNum(M)
res2 = ss.findCircleNum_dfs(M)
print(res1, res2)