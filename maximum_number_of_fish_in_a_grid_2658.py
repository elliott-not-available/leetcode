# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/?envType=daily-question&envId=2025-01-28

class Solution:
    # graph traversal
    def findMaxFish(self, grid: list[list[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        # for each point in grid find maximum path. ignore if visited
        max_fish = 0
        visited = [[False]*COLS for _ in range(ROWS)]    # (i, j)

        def find_fish(i, j):

            if ( i<0 or j<0 or i>=ROWS or j>=COLS or
                visited[i][j] or grid[i][j] == 0
            ):
                return 0
            
            visited[i][j] = True
            neighbours = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
            score = grid[i][j]

            for nr, nc in neighbours:
                    score += find_fish(nr, nc)
            
            return score

        for i in range(ROWS):
            for j in range(COLS):
                if visited[i][j] or grid[i][j] == 0:
                    continue
                max_fish = max(max_fish, find_fish(i, j))

        return max_fish
        