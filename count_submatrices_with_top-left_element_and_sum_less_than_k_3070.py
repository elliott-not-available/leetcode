# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/?envType=daily-question&envId=2026-03-18

class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        pre = [0]*cols
        res = 0

        for r in range(rows):
            r_sum = 0
            for c in range(cols):
                pre[c] += grid[r][c]
                r_sum += pre[c]
                if r_sum<=k:
                    res += 1

        return res