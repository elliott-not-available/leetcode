# https://leetcode.com/problems/minimum-cost-path-with-teleportations/description/?envType=daily-question&envId=2026-01-28

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:

        m,n = len(grid), len(grid[0])
        # list of grid indexs
        points = [(i, j) for i in range(m) for j in range(n)]
        # sort index's via their cost value
        points.sort(key=lambda p: grid[p[0]][p[1]])
        #cost of each point
        cost = [[float('inf')] * n for _ in range(m)]

        for t in range(k+1):
            min_c = float("inf")
            j = 0

            for i in range(len(points)):
                min_c = min(min_c, cost[points[i][0]][points[i][1]])

                if (
                    i + 1 < len(points)
                    and grid[points[i][0]][points[i][1]]
                    == grid[points[i+1][0]][points[i+1][1]]
                ):
                    i += 1
                    continue

                for r in range(j, i+1):
                    cost[points[r][0]][points[r][1]] = min_c
                
                j = i + 1

            for i in range(m-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if i==(m-1) and j==(n-1):
                        cost[i][j] = 0
                        continue
                    if i!=(m-1):
                        cost[i][j] = min(
                            cost[i][j], cost[i+1][j] + grid[i+1][j]
                        )
                    if j!=(n-1):
                        cost[i][j] = min(
                            cost[i][j], cost[i][j+1] + grid[i][j+1]
                        )

        return cost[0][0]