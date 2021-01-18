from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # all items in a group
        group_items = [[] for _ in range(n+m)]
        # graph between different groups
        group_g = [[] for _ in range(n+m)] 
        # graph in same group
        item_g = [[] for _ in range(n)]

        other_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = other_id
                other_id += 1
            group_items[group[i]].append(i)

        for i, befs in enumerate(beforeItems):
            cur_gid = group[i]
            for bef in befs:
                bef_gid = group[bef]
                if cur_gid == bef_gid:
                    item_g[bef].append(i)
                else:
                    group_g[bef_gid].append(cur_gid)
        # print(group_items)
        # print(item_g)
        # print(group_g)

        def dfs(i, used, sorts, G):
            if used[i] == 1:
                return False
            if used[i] == 2:
                return True
            used[i] = 1
            for j in G[i]:
                if not dfs(j, used, sorts, G):
                    return False
            sorts.append(i)
            used[i] = 2
            return True

        def t_sort(n_node, G):
            sorts = []
            used = [0] * n_node
            for i in range(n_node):
                if not dfs(i, used, sorts, G):
                    return []
            return sorts

        # sort in all groups
        group_sorts = t_sort(n+m, group_g)
        group_sorts = group_sorts[::-1]
        # print(group_sorts)

        # sort in every group
        final_sorts = []
        used = [0] * n
        for gid in group_sorts:
            if not group_items[gid]:
                continue
            sorts = []
            for item in group_items[gid]:
                if not dfs(item, used, sorts,item_g):
                    return []
            final_sorts.extend(sorts[::-1])
            
        return final_sorts


if __name__ == '__main__':
    # n=5
    # m=5
    # group= [2,0,-1,3,0]
    # beforeItems=[[2,1,3],[2,4],[],[],[]]

    # n = 8
    # m = 2
    # group = [-1,-1,1,0,0,1,0,-1]
    # beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]

    # n=3
    # m=1
    # group =[-1,0,-1]
    # beforeItems=[[],[0],[1]]


    n=8
    m=2
    group=[-1,-1,1,0,0,1,0,-1]
    beforeItems=[[3],[6,0],[5],[6],[3,6,7],[],[],[]]

    res = Solution().sortItems(n, m, group, beforeItems)
    print(res)