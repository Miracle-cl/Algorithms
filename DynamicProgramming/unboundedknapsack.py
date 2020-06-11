from typing import List
import math

def zero_one_pack(max_weigt: int, weights: List[int], values: List[int]) -> int:
    # 0-1 knapsack
    num = len(weights)
    dp = [0] * (1+max_weight)

    for i in range(1, 1+num):
        wi = weights[i-1]
        vi = values[i-1]
        for j in range(max_weight, wi-1, -1):
            dp[j] = max(dp[j], dp[j-wi]+vi)
        # print(dp)
    return dp[-1]


class UnboundedKnapsack:
    # N is num of products, W is Volume of knapsack
    @staticmethod
    def max_value(max_weight: int, weights: List[int], values: List[int]) -> int:
        # 2^x < 10 --> [1]: [1,2,4,8]
        # 5 * 2^x < 10 --> [5]: [5,10]
        # weights [1,5] --> [1,2,4,8,5,10]
        # values [1,3] --> [1,2,4,8,3,6]
        res = zero_one_pack(max_weight, [1,2,4,8,5,10], [1,2,4,8,3,6])
        return res

    @staticmethod
    def max_value_less_space(max_weight: int, weights: List[int], values: List[int]) -> int:
        num = len(weights)
        # dp[i]: max value of weight i
        dp = [0 for _ in range(1+max_weight)]

        for i in range(1, 1+max_weight):
            for j in range(num):
                if weights[j] <= i:
                    dp[i] = max(dp[i], dp[i-weights[j]]+values[j])
        return dp[-1]


max_weight = 10
weights = [1,5]
values = [1,3]

uk = UnboundedKnapsack()
r1 = uk.max_value(max_weight, weights, values)
r2 = uk.max_value_less_space(max_weight, weights, values)
print(r1, r2)
