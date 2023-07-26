from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        length = len(nums)

        def dfs(index: int, path: List[int] = []):
            results.append(path)
            for i in range(index, length):
                dfs(i + 1, path + [nums[i]])

        dfs(0)
        return results
