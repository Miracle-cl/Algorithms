class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # g[i][j] : max length of same suffix endswith s[i] & t[j]
        # f[i][j]: num of match conditions substr endswith s[i] & t[j]
        f = [[0] * n for _ in range(m)]
        g = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    g[i][j] = 1 + g[i-1][j-1] if i>0 and j>0 else 1
                # else
                #     g[i][j] = 0
                
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    f[i][j] = f[i-1][j-1] if i>0 and j>0 else 0
                else:
                    f[i][j] = g[i-1][j-1] + 1 if i>0 and j>0 else 1
        return sum(sum(f[i]) for i in range(m))



if __name__ == '__main__':
    s = 'abe'
    t = 'bbc'
    solu = Solution()
    res = solu.countSubstrings(s, t)
    print(res)