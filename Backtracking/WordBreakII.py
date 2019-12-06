from typing import List
from collections import defaultdict
# from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mem = defaultdict(list)
        # for w in wordDict:
        #     mem[w].append(w)
        return self.backtrack(s, set(wordDict), mem)

    def backtrack(self, s, wordset, mem):
        if s in mem:
            return mem[s]

        res = []
        if s in wordset:
            res.append(s)
        for w in wordset:
            if s.startswith(w):
                res += [w + ' ' + post for post in self.backtrack(s[len(w):], wordset, mem)]
        mem[s] = res
        return res


if __name__ == '__main__':
    solu = Solution()
    # s = "catsanddogsand"
    # wordDict = ["cat", "cats", "and", "sand", "dog", "dogs"]
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    s = "aaaaaaa"
    wordDict = ["aaaa","aa","a"]
    res = solu.wordBreak(s, wordDict)
    print(res)