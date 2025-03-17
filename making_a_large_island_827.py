# https://leetcode.com/problems/making-a-large-island/?envType=daily-question&envId=2025-01-31
from collections import defaultdict


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        N = len(grid)

        def out_of_bounds(r, c):
            return (
                r < 0 or c < 0 or r == N or c == N
            )
        
        def dfs(r, c, label):
            if (
                out_of_bounds(r,c) or
                grid[r][c] != 1
            ):
                return 0
            grid[r][c] = label
            size = 1

            nei = [[r+1, c], [r, c+1], [r-1, c],[r, c-1]]
            for nr, nc in nei:
                size += dfs(nr, nc, label)
            return size
        
        size = defaultdict(int)
        label = 2
        res = 0
        # calculate island areas and give unique labels
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    is_size = dfs(r,c,label)
                    res = max(res, is_size)
                    size[label] = is_size
                    label += 1

        def connect(r, c):
            nei = [[r+1, c], [r, c+1], [r-1, c],[r, c-1]]
            visited = set()
            res = 1

            for nr, nc in nei:
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visited:
                    res += size[grid[nr][nc]]
                    visited.add(grid[nr][nc])
            return res

        # res = 0 if not size else max(size.values())
        # flip each water and find max
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r,c))
        return res