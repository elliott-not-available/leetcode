# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/?envType=daily-question&envId=2026-03-19
# from collections import Counter
class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        sum_x = [0] * cols
        sum_y = [0] * cols

        res = 0

        for r in range(rows):
            x = 0
            y = 0

            for c in range(cols):
                if grid[r][c] == 'X':
                    x += 1
                if grid[r][c] == 'Y':
                    y += 1

                sum_x[c] += x
                sum_y[c] += y

                if sum_x[c] > 0 and sum_x[c]==sum_y[c]:
                    res += 1
        return res