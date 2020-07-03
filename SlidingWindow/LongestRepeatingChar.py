from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # a little slower 
        length = len(s)
        i = j = 0
        maxl = 0
        cnt = Counter()

        while i < length and j < length:
            more = cnt.most_common()[0][1] if cnt else 0
            less = j - i - more
            if less <= k:
                maxl = max(maxl, j - i)
                cnt[s[j]] += 1
                j += 1
            else:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    del cnt[s[i]]
                i += 1
            # print(i, j, cnt, maxl)

        more = cnt.most_common()[0][1] if cnt else 0
        less = j - i - more
        if less <= k:
            maxl = max(maxl, j - i)
        return maxl

    def characterReplacement_1(self, s: str, k: int) -> int:
        # faster
        length = len(s)
        i = j = 0
        maxl = 0
        more = 0 # most common character: cal faster
        cnt = Counter()

        while i < length and j < length:
            cnt[s[j]] += 1 # small window is not necessary
            j += 1
            more = max(more, cnt[s[j-1]])
            less = j - i - more
            if less <= k:
                maxl = max(maxl, j - i)
            else:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    del cnt[s[i]]
                i += 1
            # print(i, j, cnt, maxl)

        more = max(more, cnt[s[j-1]] if cnt else 0)
        less = j - i - more
        if less <= k:
            maxl = max(maxl, j - i)
        return maxl


# s = 'ABAB'
# k = 2
s = 'AABABBA'
k = 1