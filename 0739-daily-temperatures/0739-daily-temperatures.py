from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for day, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                s_day = stack.pop()[0]
                result[s_day] = day - s_day
            stack.append((day, t))
        return result
