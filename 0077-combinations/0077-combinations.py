from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(start: int):
            if len(prev_elements) == k:
                results.append([*prev_elements])
                return
            for i in range(start, n + 1):
                prev_elements.append(i)
                dfs(i + 1)
                prev_elements.pop()

        dfs(1)
        return results
