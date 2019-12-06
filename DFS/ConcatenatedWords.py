from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # TLE
        res = []
        if len(words) < 3:
            return res
        mem = dict()
        for w in words:
            wordset = set(words)
            wordset.discard(w)
            if self.recursive(w, wordset, mem):
                res.append(w)
            # print(mem)
        return res
    
    def recursive(self, s, words, mem):
        if s in mem:
            return mem[s]

        for w in words:
            if s.startswith(w) and (s[len(w):] in words or self.recursive(s[len(w):], words, mem)):
                mem[s] = 1
                return 1
        mem[s] = 0
        return 0


if __name__ == '__main__':
    solu = Solution()
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    res = solu.findAllConcatenatedWordsInADict(words)
    print(res)