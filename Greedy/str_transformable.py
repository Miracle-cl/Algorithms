from collections import defaultdict, deque
# from pprint import pprint


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        idx = defaultdict(deque)
        for i, c in enumerate(s):
            idx[int(c)].append(i)

        for c in t:
            c = int(c)
            if not idx[c]:
                return False
            ic = idx[c].popleft()
            for j in range(c):
                if idx[j] and idx[j][0] < ic:
                    return False
        return True


# s = "84532"
# t = "34852"
s = "12345"
t = "12435"