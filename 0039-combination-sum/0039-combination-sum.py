from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(elements: List[int], start_index: int = 0, sum: int = 0):
            if sum == target:
                results.append([*elements])
            if sum >= target:
                return
            for i in range(start_index, len(candidates)):
                dfs(elements + [candidates[i]], i, sum + candidates[i])

        dfs([])
        return results
