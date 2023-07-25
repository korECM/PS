from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements: List[int]):
            if len(elements) == 0:
                results.append(prev_elements[:])
                return
            for i in range(len(elements)):
                prev_elements.append(elements[i])
                dfs(elements[:i] + elements[i + 1:])
                prev_elements.pop()

        dfs(nums)
        return results
