from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # prefix sum & brute force: 356ms
        mode = 10 ** 9 + 7
        pre_sum = [0] + nums
        for i in range(1, 1+n):
            pre_sum[i] += pre_sum[i-1]
            
        res = []
        for i in range(n):
            for j in range(i+1, n+1):
                res.append(pre_sum[j] - pre_sum[i])
        res.sort()
        return sum(res[left-1: right]) % mode

    def rangeSum_1(self, nums: List[int], n: int, left: int, right: int) -> int:
        # binary search : 300 ms
        mode = 10 ** 9 + 7
        pre_sum = [0] + nums
        for i in range(1, 1+n):
            pre_sum[i] += pre_sum[i-1]

        def f(i, j):
            return pre_sum[j+1] - pre_sum[i]

        def count(target):
            cnt = 0
            j = 0
            for i in range(n):
                while j < n and f(i, j) <= target:
                    j += 1
                cnt += j - i
            return cnt

        def get_sum(target):
            # O(n2) : math solution need less time
            ans = 0
            j = 0
            cnt = 0
            for i in range(n):
                for j in range(i, n):
                    if f(i, j) <= target:
                        ans += f(i, j)
                        cnt += 1
                    else:
                        break
                ans = ans % mode
            return ans, cnt

        def binary_search(k, l, r):
            while l < r:
                mid = (l + r) // 2
                cnt = count(mid)
                if cnt < k:
                    l = mid+1
                else:
                    r = mid
            # as duplicate elems, not get_sum(l)
            sum_, cnt_ = get_sum(l-1)
            sum_ += l * (k - cnt_) 
            return sum_

        ll, rr = min(nums), sum(nums)+1

        ls = binary_search(left-1, ll, rr) if left > 1 else 0
        rs = binary_search(right, ll, rr)
        # print(ls, rs)
        return rs - ls


if __name__ == '__main__':
    nums = [7,5,8,5,6,4,3,3]
    n = 8
    left = 2
    right = 6
    ss = Solution()
    res0 = ss.rangeSum(nums, n, left, right)
    res1 = ss.rangeSum_1(nums, n, left, right)
    print(res0, res1)