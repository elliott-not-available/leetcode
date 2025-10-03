# https://leetcode.com/problems/trapping-rain-water-ii/?envType=daily-question&envId=2025-10-03
from heapq import heappush, heappop
class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        ## ended up using previous attempt to help alot
        
        # visited map + dirs
        rows = len(heightMap)
        cols = len(heightMap[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        min_heap = []

        for r in range(rows):
            for c in range(cols):
                # just boundary
                if r in [0, rows-1] or c in [0,cols-1]:
            
                    heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = 1

        def _is_valid(x,y):
                    v = 0 <= x < rows and 0 <= y < cols and not visited[x][y]
                    # print(f"{x}, {y} is {v}")
                    return v

        res = 0
        max_h = -1
        # print(visited)

        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h

            neighbs = [(r+a, c+b) for a,b in dirs]

            for n_r, n_c in neighbs:
                if _is_valid(n_r, n_c):
                    heappush(min_heap, (heightMap[n_r][n_c], n_r, n_c))
                    visited[n_r][n_c] = 1

        return res