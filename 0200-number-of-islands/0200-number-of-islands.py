from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] != '1':
                return
            grid[y][x] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    dfs(x, y)
                    count += 1
        return count
