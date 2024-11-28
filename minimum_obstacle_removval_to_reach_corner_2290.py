# minimum_obstacle_removval_to_reach_corner_2290
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/?envType=daily-question&envId=2024-11-28
from collections import deque, defaultdict

class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        # deque
        m = len(grid)
        n = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque()

        cnt = 0
        i = 0
        j = 0

        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True

        q.append((i, j, cnt))

        while q:
            cur_i, cur_j, cnt = q.popleft()

            if cur_i == m-1 and cur_j == n -1:
                return cnt

            for dx,dy in directions:
                ni,nj = cur_i+dx, cur_j+dy

                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True

                    if grid[ni][nj] == 0:
                        q.appendleft((ni, nj, cnt))
                    else:
                        q.append((ni, nj, cnt+1))
        return False



