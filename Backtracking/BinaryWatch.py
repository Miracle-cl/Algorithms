from typing import List

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return ['0:00']
        if num >= 9: # > 10
            return []

        hs = [1,2,4,8]
        ms = [1,2,4,8,16,32]
        
        tmp = []
        res = []
        
        def backtrack(start, num, limit, size, _sum, selects):
            if num == 0:
                if _sum < limit:
                    tmp.append(_sum)
                return
            for i in range(start, size):
                backtrack(i+1, num-1, limit, size, _sum+selects[i], selects)

        for hour in range(max(0, num-6), min(num+1, 5)):
            minute = min(num-hour, 6)
            # print(hour, minute)
            # continue
            backtrack(0, hour, 12, 4, 0, hs)
            sel_hs = tmp.copy()
            tmp.clear()
            backtrack(0, minute, 60, 6, 0, ms)
            res += ['{}:{}'.format(h, str(m) if m > 9 else '0'+str(m)) 
                    for h in sel_hs for m in tmp]
            tmp.clear()

        return res


if __name__ == '__main__':
    solu = Solution()
    num = 1
    res = solu.readBinaryWatch(num)
    print(res)