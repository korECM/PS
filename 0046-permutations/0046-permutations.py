from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(visited: List[int]):
            if len(visited) == len(nums):
                results.append(list(map(lambda x: nums[x], visited)))
            for j in range(len(nums)):
                if j not in visited:
                    dfs(visited + [j])

        for i in range(len(nums)):
            dfs([i])
        return results
