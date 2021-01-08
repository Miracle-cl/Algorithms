from typing import List
from pprint import pprint
from collections import deque, Counter
import heapq, math
import bisect



# 00011000
# 00011010


# 00011001
# 10
# 01

binary = "0000011010101011111001001"


chs = [ch for ch in binary]

n = len(chs)
i = 0

print(''.join(chs))
# i ==0 j == 0
# i - 1
# i+1 - 0
# j - 1

cnt = Counter("0000011010101011111001001")

s1  = "1111111111110111111111111"
print(cnt)
print(s1.index('0'))