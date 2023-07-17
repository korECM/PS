from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left_mem = [100000] * len(prices)
        right_mem = [0] * len(prices)

        min_value = 100000
        for i in range(len(prices)):
            min_value = min(min_value, prices[i])
            left_mem[i] = min_value
        max_value = 0
        for i in range(len(prices) - 1, -1, -1):
            max_value = max(max_value, prices[i])
            right_mem[i] = max_value

        for i in range(len(left_mem)):
            max_profit = max(max_profit, right_mem[i] - left_mem[i])

        print(left_mem, right_mem)

        return max_profit
