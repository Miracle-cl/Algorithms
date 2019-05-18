s = "babgbag"
t = "bag"

def numDistinct(s, t):
    if not t:
        return 1;
    if not s:
        return 0;

    row = len(t) + 1
    column = len(s) + 1
    dp = [[0] * column for i in range(row)]
    for i in range(column):
        dp[0][i] = 1

    for i in range(1, row):
        for j in range(1, column):
            dp[i][j] = dp[i][j-1] + (dp[i-1][j-1] if s[j-1] == t[i-1] else 0)

    return dp[row-1][column-1]

print(numDistinct(s, t))
