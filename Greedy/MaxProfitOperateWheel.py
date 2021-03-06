from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1
        max_ = float('-inf')
        profit = 0
        n = len(customers)
        turns = -1
        waiting = 0
        for i, c in enumerate(customers, 1):
            waiting += c
            if waiting <= 0:
                profit -= runningCost
            elif waiting < 4:
                profit += boardingCost * waiting - runningCost
                waiting = 0
            else:
                profit += boardingCost * 4 - runningCost
                waiting -= 4
            if profit > max_:
                max_ = profit
                turns = i
        if waiting > 0:
            _t = waiting // 4
            p1 = profit + boardingCost * _t * 4 - runningCost * _t 
            p2 = profit + boardingCost * waiting - runningCost * (_t + 1)
            if p2 > p1 and p2 > max_:
                turns = n + _t + 1
                max_ = p2
            elif p1 > max_:
                turns = n + _t
                max_ = p1
        return turns if max_ > 0 else -1


# customers=[8,3]
# boardingCost=5
# runningCost=6 # 3

customers=[10,10,1,0,0]
boardingCost=4
runningCost=4 # 5

# customers=[0,43,37,9,23,35,18,7,45,3,8,24,1,6,37,2,38,15,1,14,39,27,4,25,27,33,43,8,44,30,38,40,20,5,17,27,
#            43,11,6,2,30,49,30,25,32,3,18,23,45,43,30,14,41,17,42,42,44,38,18,26,32,48,37,5,37,21,2,9,48,48,40,
#            45,25,30,49,41,4,48,40,29,23,17,7,5,44,23,43,9,35,26,44,3,26,16,31,11,9,4,28,49,43,39,9,39,37,7,6,
#            7,16,1,30,2,4,43,23,16,39,5,30,23,39,29,31,26,35,15,5,11,45,44,45,43,4,24,40,7,36,10,10,18,6,20,13,
#            11,20,3,32,49,34,41,13,11,3,13,0,13,44,48,43,23,12,23,2]
# boardingCost=43
# runningCost=54 # 993

# customers, boardingCost, runningCost = [10,10,6,4,7], 3, 8 # 9