from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements: List[int]):
            if len(elements) == 0:
                results.append([*prev_elements])
                return
            prev_elements.append(elements[0])
            dfs(elements[1:])
            prev_elements.pop()
            dfs(elements[1:])

        dfs(nums)
        return results
