class Solution():
    def __init__(self):
        pass

    def min_cut(self, str):
        length = len(str)
        is_pal_matrix = [[0] * length for _ in range(length)]
        dp = [length-1-i for i in range(length)] + [-1]

        for i in range(length-1, -1, -1):
            for j in range(i, length):
                if str[i] == str[j] and (j-i <= 1 or is_pal_matrix[i+1][j-1]):
                    is_pal_matrix[i][j] = 1
                    dp[i] = min(dp[i], dp[j+1] + 1)
        print(dp)
        return dp[0]

solu = Solution()
str = "abcbabaa"
print(solu.min_cut(str))
