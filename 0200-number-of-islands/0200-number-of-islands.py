from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    self.dfs(grid, x, y)
                    count += 1
        return count

    def dfs(self, grid, x, y):
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]) or grid[y][x] != '1':
            return
        grid[y][x] = '0'
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x, y - 1)
