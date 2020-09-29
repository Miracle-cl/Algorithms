from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        r, c = len(targetGrid), len(targetGrid[0])
    
        # find rectangle of same color
        rect = {} # [left_bottom, right_top]
        for i in range(r):
            for j in range(c):
                color = targetGrid[i][j]
                if color not in rect:
                    rect[color] = [i, j, i, j]
                else:
                    if i < rect[color][0]:
                        rect[color][0] = i
                    elif i > rect[color][2]:
                        rect[color][2] = i

                    if j < rect[color][1]:
                        rect[color][1] = j
                    elif j > rect[color][3]:
                        rect[color][3] = j

        # create graph: if color v in color u rectangle, then u->v
        nodes = len(rect)
        graph = {}
        used = {}
        for color, pts in rect.items():
            lbi, lbj, rti, rtj = pts
            graph[color] = set()
            used[color] = 0
            for i in range(lbi, rti+1):
                for j in range(lbj, rtj+1):
                    if targetGrid[i][j] == color:
                        continue
                    graph[color].add(targetGrid[i][j])

        # find if cycle in graph <-> toplogical sort
        def dfs(u):
            if used[u] == 1:
                return False
            if used[u] == 2:
                return True
            used[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            used[u] = 2
            return True

        for c in rect.keys():
            if not dfs(c):
                return False
        return True


# targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
targetGrid = [[1,1,1],[3,1,3]]