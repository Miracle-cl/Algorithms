from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0 or (not coins):
            return -1
        if amount == 0:
            return 0

        dp = [-1] * (1 + amount)
        dp[0] = 0
        for a in range(1, 1+amount):
            for c in coins:
                if a-c >= 0 and dp[a-c] > -1:
                    if dp[a]==-1 or dp[a] > dp[a-c]+1:
                        dp[a] = dp[a-c] + 1
        return dp[-1]

    def coinChange_bfs(self, coins: List[int], amount: int) -> int:
        q = [amount]
        visited = set() # if not TLE
        level = 0
        levels = []
        while q:
            nex_q = set() # if list then Memory limit exceeded
            level += 1
            while q:
                tmp = q.pop()
                if tmp in visited:
                    continue
                for c in coins:
                    if tmp % c == 0:
                        levels.append(level + tmp // c - 1)
                    elif c < tmp:
                        nex_q.add(tmp-c)
                visited.add(tmp)
            q = list(nex_q)
        return min(levels) if levels else -1

if __name__ == '__main__':
    import time
    solu = Solution()
    # coins = [186,419,83,408]
    # amount = 6249
    coins = [5,306,188,467,494]
    amount = 7047
    t0 = time.time()
    res1 = solu.coinChange_bfs(coins, amount)
    t1 = time.time()
    res2 = solu.coinChange(coins, amount)
    t2 = time.time()
    print(res1, t1-t0)
    print(res2, t2-t1)