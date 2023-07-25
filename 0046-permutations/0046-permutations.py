from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(visited: List[int], results: List[List[int]]):
            if len(visited) == len(nums):
                results.append(list(map(lambda x: nums[x], visited)))
            for i in range(len(nums)):
                if i in visited:
                    continue
                dfs(visited + [i], results)

        results = []
        for i in range(len(nums)):
            dfs([i], results)
        return results
