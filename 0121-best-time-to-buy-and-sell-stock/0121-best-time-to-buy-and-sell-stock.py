from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = 100000
        for price in prices:
            min_value = min(price, min_value)
            max_profit = max(max_profit, price - min_value)
        return max_profit
