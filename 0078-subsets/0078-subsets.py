from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(elements: List[int], start_index: int, acc: List[int] = []):
            if len(elements) == start_index:
                results.append(acc)
                return
            dfs(elements, start_index + 1, acc + [elements[start_index]])
            dfs(elements, start_index + 1, acc)

        dfs(nums, 0)
        return results
