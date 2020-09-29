class Solution:
    def minimumOperations_2(self, leaves: str) -> int:
        prefix = [0] # prefix[x]: reds of [0, x)
        for c in leaves:
            if c == 'r':
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1])

        # three parts [0, i), [i, j), [j, n) 
        # modifies = i - prefix[i];  prefix[j] - prefix[i];  (n-j) - (prefix[n] - prefix[j])
        #       = (n - prefix[n]) + (i - 2*prefix[i]) - (j - 2*prefix[j])
        n = len(leaves)

        # j from n-1 to 2
        ans = float('inf')
        for j in range(n-1, 1, -1):
            minj = float('inf')
            _j = j - 2*prefix[j]
            for i in range(1, j):
                minj = min((i - 2*prefix[i]) - _j, minj) # repeat calculation
            ans = min(minj, ans)
            
        return ans + n - prefix[n]


    def minimumOperations_1(self, leaves: str) -> int:
        prefix = [0] # prefix[x]: reds of [0, x)
        for c in leaves:
            if c == 'r':
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1])

        # three parts [0, i), [i, j), [j, n) 
        # modifies = i - prefix[i];  prefix[j] - prefix[i];  (n-j) - (prefix[n] - prefix[j])
        #       = (n - prefix[n]) + (i - 2*prefix[i]) - (j - 2*prefix[j])
        n = len(leaves)

        # dp[x]: min i-2p[i] from 0 to x
        dp = [float('inf')] * n
        for i in range(1, n-1):
            dp[i] = min(i - 2 * prefix[i], dp[i-1])

        ans = float('inf')
        for j in range(n-1, 1, -1):
            ans = min(ans, dp[j-1] - (j - 2*prefix[j]))
            
        return ans + n - prefix[n]


# LCP 19. 秋叶收藏集
leaves = "rrryyyrryyyrr"  # 2
leaves = "ryr" # 0

ss = Solution()
res = ss.minimumOperations_1(leaves)
print(res)