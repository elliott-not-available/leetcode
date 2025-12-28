# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/?envType=daily-question&envId=2025-12-28

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            cur = 0
            for j in range(n):
                if grid[i][j] < 0:
                    cur = (n-j)
                    break
            
            if cur == n:
                # print(i, j, "full", n, (m-i))
                res += n*(m-i)
                break
            else:
                # print(i, j, cur)
                res += cur

        return res
        