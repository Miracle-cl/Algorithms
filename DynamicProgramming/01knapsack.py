from typing import List



class KnapSackProblem:
    # N is num of products, W is Volume of knapsack
    @staticmethod
    def max_value(max_weight: int, weights: List[int], values: List[int]) -> int:
        # Time: O(NW), Space: O(NW)
        num = len(weights)
        # dp[i][j]: max value with first i items and total volume is j 
        # (total volume >= actual weight of products)
        dp = [[0] * (1+max_weight) for _ in range(1+num)]

        for i in range(1, 1+num):
            wi = weights[i-1]
            vi = values[i-1]
            for j in range(1, 1+max_weight):
                if j >= wi:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-wi]+vi)
                else:
                    dp[i][j] = dp[i-1][j]
            # break
        print(dp)
        return dp[-1][-1]

    @staticmethod
    def max_value_less_space(max_weight: int, weights: List[int], values: List[int]) -> int:
        # Time: O(NW), Space: O(W)
        num = len(weights)
        dp = [0] * (1+max_weight)

        for i in range(1, 1+num):
            wi = weights[i-1]
            vi = values[i-1]
            for j in range(max_weight, wi-1, -1):
                dp[j] = max(dp[j], dp[j-wi]+vi)
            # print(dp)
        return dp[-1]


if __name__ == '__main__':
    # max_weight = 100

    # weights = [77, 21, 29, 50, 99]
    # values = [92, 22, 87, 46, 90]

    max_weight = 4
    weights = [1,1,2,2]
    values = [1,2,4,5]

    # weights = [2,2,1,1,]
    # values = [4,5,1,2,]

    ksp = KnapSackProblem()
    r1 = ksp.max_value(max_weight, weights, values)
    r2 = ksp.max_value_less_space(max_weight, weights, values)
    print(r1, r2)