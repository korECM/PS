from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements: List[int]):
            if len(elements) == 0:
                results.append(prev_elements[:])
            for i in range(len(elements)):
                next_elements = elements[:i] + elements[i + 1:]

                prev_elements.append(elements[i])
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results
