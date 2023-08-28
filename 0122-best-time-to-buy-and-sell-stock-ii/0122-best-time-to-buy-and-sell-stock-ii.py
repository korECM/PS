from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur: Optional[int] = None
        for a, b in zip(prices, prices[1:] + [prices[-1]]):
            if cur is not None and cur < a:
                profit += a - cur
                cur = None
            if cur is None and a < b:
                cur = a
        return profit
