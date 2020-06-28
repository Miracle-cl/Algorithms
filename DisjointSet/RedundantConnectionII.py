from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # case 1: (no duplicate parents) remove first edge creating the loop
        # case 2: (duplicate parents) [(u1, v), (u2, v)]; if u1 in loop then rm u1, else rm u2
        n = 1 + len(edges)
        roots = list(range(n))
        parents = list(range(n))

        ans = [] # store duplicate parents
        for i, (u, v) in enumerate(edges):
            # u -> v
            if parents[v] != v:
                # print(u, v)
                ans.append([parents[v], v])
                ans.append([u, v])
                edges[i] = [-1, -1]
            else:
                parents[v] = u

        # parents, ans, edges
        def _find(i):
            if i != roots[i]:
                roots[i] = _find(roots[i])
            return roots[i]

        for u, v in edges:
            if u < 0:
                continue
            ru = _find(u)
            rv = _find(v)
            if ru == rv:
                # second edge of same parent is -1 now
                return ans[0] if ans else [u, v]
            roots[ru] = rv

        return ans[1]


# test cases:
# [[1,2], [1,3], [2,3]] -> [2,3]
# [[1,2], [2,3], [3,4], [4,1], [1,5]] -> [4,1]
# [[2,1],[3,1],[4,2],[1,4]] -> [2,1]