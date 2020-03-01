class Solution:
    def isMatch0(self, s: str, p: str) -> bool:
        r, c = len(p)+1, len(s)+1
        dp = [[0] * c for _ in range(r)]
        dp[0][0] = 1
        for i in range(1, r):
            if p[i-1] == '*':
                dp[i][0] = dp[i-1][0]
        for i in range(1, r):
            for j in range(1, c):
                if p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif p[i-1] == '?' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]          
        
        return bool(dp[-1][-1])

    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        last_star = -1
        
        while i < len(s):
            if j < len(p) and p[j] =='*' :
                last_star = j
                last_match = i
                j += 1
            elif j < len(p) and (s[i] == p[j] or p[j]=='?'):
                i += 1
                j += 1
            elif last_star >= 0:
                last_match += 1
                i = last_match 
                j = last_star + 1
            else:
                return False
            
        while j<len(p) and p[j]=='*':
            j += 1
        
        return j==len(p)


if __name__ == '__main__':
    s = "adceb"
    p = "*a*b"
    solu = Solution()
    res = solu.isMatch(s, p)
    print(res)