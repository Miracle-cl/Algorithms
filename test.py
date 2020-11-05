from typing import List
from pprint import pprint
from collections import deque
import heapq, math
import bisect


locations = [2,3,6,8,4]
start, finish, fuel = 1, 3, 5

# locations = [2,1,5]
# start, finish, fuel = 0,0,3

# class Solution:


def bt(k, h, v, s):
    if k == 0:
        print(s)
        return 
    if h == 0 and v == 0:
        k -= 1
        return
    if h > 0:
        bt(h-1, v, s + 'H')
    if v > 0:
        bt(h, v-1, s + 'V')

bt(1,3,3,'')