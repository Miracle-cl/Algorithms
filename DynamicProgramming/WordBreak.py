class Solution:
    def wordBreak(self, s, wordDict):
        # s: str, wordDict: List[str]
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = 1
                    break
        return dp[-1]

    def wordBreak_bt(self, s, wordDict):
        # backtrack ?
        index_checked = set()
        def helper(index):
            if index==len(s):
                return True

            if index in index_checked:
                return False

            for word in wordDict:
                n = len(word)
                if word == s[index:index+n]:
                    if helper(index+n):
                        return True

            index_checked.add(index)
            # print(index_checked)
            return False
        return helper(0)


s = 'applepenapplepe'
wordDict = ['apple', 'pen']
solu = Solution()
res = solu.wordBreak_bt(s, wordDict)
print(res)
# print(bool(1), bool(2), bool(0))
