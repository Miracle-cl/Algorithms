from collections import defaultdict


class Solution:
    def racecar_bfs(self, target: int) -> int:
        thred = 2 * target
        pos, spe = 0, 1
        pos_spe = defaultdict(set)
        q = [(pos, spe)]
        step = 0
        while q:
            nxt = []
            step += 1
            for p1, s1 in q:
                # forward
                p_f = p1 + s1
                s_f = 2 * s1
                if not (p_f in pos_spe and s_f in pos_spe[p_f]): # not visited
                    if -target < p_f < thred and s_f < thred: # not back to the start
                        nxt.append((p_f, s_f))
                # reverse
                p_b = p1
                s_b = 1 if s_f < 0 else -1
                if not (p_b in pos_spe and s_b in pos_spe[p_b]):
                    if -target < p_b < thred:
                        nxt.append((p_b, s_b))
                if p_f == target or p_b == target:
                    return step
                pos_spe[p_f].add(s_f)
                pos_spe[p_b].add(s_b)
            q = nxt
        return step


if __name__ == "__main__":
    target = 6
    ss = Solution()
    res1 = ss.racecar_bfs(target)
    print(res1)