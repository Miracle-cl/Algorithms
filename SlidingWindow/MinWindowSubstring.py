from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # check is O(len(cnt)), slower
        ori = Counter()
        cnt = Counter()
        def check():
            for k, v in ori.items():
                if cnt[k] < v:
                    return False
            return True

        for c in t:
            ori[c] += 1

        l, r = 0, -1
        ans_len = float('inf')
        ansl = -1
        slen = len(s)
        for r in range(slen):
            if s[r] in ori:
                cnt[s[r]] += 1
                while check() and l <= r:
                    if r - l + 1 < ans_len:
                        ans_len = r - l + 1
                        ansl = l
                    if s[l] in ori:
                        cnt[s[l]] -= 1
                    l += 1

        ans = '' if ansl == -1 else s[ansl: ansl+ans_len]
        return ans

    def minWindow_optim_1(self, s: str, t: str) -> str:
        needs = Counter(t)
        windows = Counter()
        tlen = len(needs)
        match = 0
        l = 0
        min_len = len(s) + 1
        start = 0
        for r, char in enumerate(s):
            if char in needs:
                windows[char] += 1
                if windows[char] == needs[char]:
                    match += 1
                    while match == tlen and l <= r:
                        while s[l] not in needs:
                            l += 1
                        if r - l + 1 < min_len:
                            # print(l, r, windows)
                            min_len = r - l + 1
                            start = l
                        if s[l] in needs:
                            windows[s[l]] -= 1
                            if windows[s[l]] < needs[s[l]]:
                                match -= 1
                        l += 1
        return '' if min_len == len(s) + 1 else s[start:start+min_len]


if __name__ == '__main__':
    st = [("ADOBECODEBANC", "ABC"), ("bba", "ab"), ('ba', 'a'), 
          ('a', 'a'), ('ba', 'x'), ('dbadbeccodebancc', 'abcc')]
    ss = Solution()
    for s, t in st:
        print([s, t, ss.minWindow_optim_1(s, t)])