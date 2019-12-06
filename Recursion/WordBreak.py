from typing import List
from functools import lru_cache

# TLE Solution without lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.recursive(s, tuple(wordDict))
    
    @lru_cache(maxsize=128)
    def recursive(self, s, wordset):
        if not s:
            return True
        for w in wordset:
            if s.startswith(w) and self.recursive(s[len(w):], wordset):
                return True
        return False


# create memroy dict to save  recursive info
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memory = {w: 1 for w in wordDict}
        memory[''] = 1
        return self.recursive(s, set(wordDict), memory)

    def recursive(self, s, wordset, memory):
        if s in memory:
            return memory[s]
        for w in wordset:
            if s.startswith(w) and self.recursive(s[len(w):], wordset, memory):
                memory[s] = True
                return True
        memory[s] = False
        return False

if __name__ == '__main__':
    solu = Solution2()
    s = 'leetcode'
    wd = ['leet', 'code']
    res = solu.wordBreak(s, wd)
    print(res)

