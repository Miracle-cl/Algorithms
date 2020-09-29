from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        cnt = [0] * n
        for s, e, x in bookings:
            cnt[s-1] += x
            if e < n:
                cnt[e] -= x
        for i in range(1, n):
            cnt[i] += cnt[i-1]
        return cnt


bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5