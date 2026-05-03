# https://leetcode.com/problems/detect-cycles-in-2d-grid/?envType=daily-question&envId=2026-04-26

class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        # wierd dfs
        m,n = len(grid), len(grid[0])
        visited = [False] * (m*n)
        d = ((0, 1), (1,0), (0,-1), (-1,0))

        def dfs(r,c,pr,pc):
            visited[r*n + c]

            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if (nr, nc) != (pr, pc):
                    if visited[nr*n + nc] or dfs(nr, nc, r, c):
                        return True
            return False



        return any(not visited[i] and dfs(i//n, i%n, -1, -1 ) for i in range(m*n))