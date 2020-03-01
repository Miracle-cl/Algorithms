import math

class Solution:
    # bfs - faster
    def numSquares_bfs(self, n: int) -> int:
        if n < 4:
            return n
        squares = [1]
        for i in range(2, 1+n):
            ans = i * i
            if ans > n:
                break
            squares.append(ans)
        squares_set = set(squares)

        q = [n]
        lev = 1
        while q:
            nxt = set()
            for qn in q:
                if qn in squares_set:
                    return lev
                for squ in squares:
                    if qn - squ > 0:
                        nxt.add(qn - squ)
                    else:
                        break
            lev += 1
            q = nxt
        return lev

    # dp
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        dp = [-1] * (1+n)
        dp[1], dp[2], dp[3] = 1, 2, 3
        squares = [1]
        for i in range(2, 1+n):
            ans = i * i
            if ans > n:
                break
            dp[ans] = 1
            squares.append(ans)
        if dp[n] == 1:
            return 1
        
        for i in range(4, 1+n):
            if dp[i] == 1:
                continue
            minv = float('inf')
            for j in squares:
                if i - j < 1 or minv == 2:
                    break
                minv = min(minv, dp[j]+dp[i-j])

            dp[i] = minv
        return dp[n]

    # def numSquares(self, n: int) -> int:
    #     # TLE
    #     if n < 4:
    #         return n
    #     dp = [-1] * (1+n)
    #     dp[1], dp[2], dp[3] = 1, 2, 3
    #     for i in range(4, 1+n):
    #         nsqrt = math.sqrt(i)
    #         if nsqrt == int(nsqrt):
    #             dp[i] = 1
    #             continue
    #         dp[i] = min(dp[j]+dp[i-j] for j in range(1, 1+i//2))
    #     return dp[n]

    # def numSquares(self, n: int) -> int:
    #     # TLE
    #     if n < 4:
    #         return n
    #     dp = [-1] * (1+n)
    #     dp[1], dp[2], dp[3] = 1, 2, 3
    #     for i in range(2, 1+n):
    #         ans = i * i
    #         if ans > n:
    #             break
    #         dp[ans] = 1
    #     if dp[n] == 1:
    #         return 1
        
    #     for i in range(4, 1+n):
    #         if dp[i] == 1:
    #             continue
    #         dp[i] = min(dp[j]+dp[i-j] for j in range(1, 1+i//2))
    #     return dp[n]


if __name__ == '__main__':
    solu = Solution()
    n = 255
    res1 = solu.numSquares(n)
    res2 = solu.numSquares_bfs(n)
    print(res1, res2)