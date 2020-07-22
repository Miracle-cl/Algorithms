class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        dp = [[False] * (l1+1) for _ in range(l2+1)]

        # dp[i][j]: (first i elem in s2 and first j elem in s1) == (first i+j elem in s3)
        # dp[i][j] = dp[i-1][j] and s2[i] == s3[i+j]
        #         or dp[i][j-1] and s1[j] == s3[i+j]

        dp[0][0] = True
        # first row: s1
        for j in range(1, l1+1):
            dp[0][j] = True if dp[0][j-1] and s1[j-1]==s3[j-1] else False
            
        # first column: s2
        for i in range(1, l2+1):
            dp[i][0] = True if dp[i-1][0] and s2[i-1]==s3[i-1] else False
            
        for i in range(1, l2+1): # s2
            for j in range(1, l1+1): # s1
                k = i + j - 1
                if (dp[i-1][j] and s2[i-1]==s3[k]) or (dp[i][j-1] and s1[j-1]==s3[k]):
                    dp[i][j] = True
                    
        return dp[l2][l1]


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false