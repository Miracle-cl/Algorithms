from typing import List

# houses = [0,0,0,0,0]
# cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
# m = 5
# n = 2
# target = 3

# import re

# s = "pes(2019)xx"
# pattern = re.compile(r'\(\d+\)')
# b, e = pattern.search(s).span()
# print(s[:b])

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_map = dict()

        for i in range(len(names)):
            name = names[i]
            if name not in name_map:
                name_map[name] = 1
            else:
                k = name_map[name]
                while True:
                    ns = name + f'({k})'
                    if ns not in name_map:
                        names[i] = ns
                        name_map[name] = k + 1
                        name_map[ns] = 1
                        break
                    else:
                        k += 1
        return names


from collections import deque

[2,3,0,0,3,1,0,1,0,2,2]
[-1,-1,3,2,-1,-1,1,-1,2,-1,-1]