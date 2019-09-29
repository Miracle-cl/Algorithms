from typing import List
from collections import deque

def distance_bfs(adj_list: List, src: int, tar: int):
    dist = [-1] * len(adj_list)
    path = [[] for _ in range(len(adj_list))]
    unreached = True
    dist[src] = 0
    path[src] = [src]
    dq = deque([src])
    while dq and unreached:
        u = dq.popleft()
        # print(u)
        for v in adj_list[u]:
            if dist[v] == -1:
                path[v].extend(path[u] + [v])
                dist[v] = dist[u] + 1
                dq.append(v)
            if v == tar:
                unreached = False
                break
        # print(path)
    return dist[tar], path[tar]


def get_agj_list(vertex: List[int], edge: List) -> List:
    adj_list = [[] for _ in range(len(vertex))]
    for i, j in edge:
        adj_list[i].append(j)
        adj_list[j].append(i)
    return adj_list

if __name__ == '__main__':
    vertex = [0,1,2,3,4,5,6,7]
    edge = [(1,2), (1,0), (0,3), (3,7), (3,4), (7,4), (7,6), (4,6), (4,5), (5,6)]
    adj_list = get_agj_list(vertex, edge)
    dist, path = distance_bfs(adj_list, 2, 6)
    print('Distance : {}'.format(dist))
    print('Path : {}'.format(path))
