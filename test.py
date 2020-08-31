from typing import List

from collections import deque
# houses = [0,0,0,0,0]
# cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
# m = 5
# n = 2
# target = 3

# import re

# s = "pes(2019)xx"
# pattern = re.compile(r'\(\d+\)')
# b, e = pattern.search(s).span()
# print(s[:b])

# import re
# def check(s):
#     n = len(s)
#     mid = n // 2
#     if n % 2 == 0:
#         l, r = mid-1, mid
#     else:
#         l, r = mid, mid
#     while l >= 0:
#         if s[l] == s[r]:
#             l -= 1
#             r += 1
#         else:
#             return False
#     return True

# def f():
#     s = 'abcd'
#     if check(s):
#         return s
#     rev_s = s[::-1][:-1]
#     print(s, rev_s)
#     for k in range(1, len(s)):
#         tmp = rev_s[:k] + s
#         print(tmp)
#         if check(tmp):
#             return tmp
#     return ''
# print([f()])


def match(s, p):
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
        i += 1
    return ans

def build(p):
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


s = 'abcabcdababcdabcdabde'
p = 'abcdabd'
res = match(s, p)
print(res)