from typing import List


def match(s: str, p: str) -> List[str]:
    n, m = len(s), len(p)
    ans = []
    nxt = build(p) # build next table
    print(nxt)
    j = 0 # i : s; j : p
    for i in range(n):
        while j > 0 and s[i] != p[j]: # fail then jump until a match or j == 0
            j = nxt[j]
        if s[i] == p[j]: # match then check next pair (i++, j++)
            j += 1
        if j == m: # find a full match
            ans.append(i - m + 1)
            j = nxt[j] # jump as it failed
        # print(i, j)
    return ans

def build(p: str) -> List[str]:
    # nxt[i]: length of longest prefix of p[:i] that is also the suffix
    # len(nxt) = len(p) + 1
    nxt = [0, 0]
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]: # fail then jump until a match or j == 0
            j = nxt[j]
        if p[i] == p[j]:
            j += 1
        nxt.append(j)
    return nxt


# s = 'abcabcdababcdabcdabde'
# p = 'abcdabd'
s = 'aaaaa'
p = 'aa'
res = match(s, p)
print(res)