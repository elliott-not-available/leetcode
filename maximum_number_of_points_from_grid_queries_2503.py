# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/?envType=daily-question&envId=2025-03-28

from heapq import heappop, heappush

class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        
        visited = set([(0,0)])

        m = [(q, i) for i, q in enumerate(queries)]
        m.sort()

        rows, cols = len(grid), len(grid[0])

        min_heap = [(grid[0][0], 0, 0)]

        res = [0] * len(queries)
        p = 0

        for limit, index in m:

            while min_heap and min_heap[0][0] < limit:
                _, r, c = heappop(min_heap)
                p += 1
                neighbours = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
                for nr, nc in neighbours:
                    if (
                        (nr,nc) not in visited and
                        0 <= nr < rows and
                        0 <= nc < cols
                    ):    
                        visited.add((nr, nc))
                        heappush(min_heap, (grid[nr][nc], nr, nc))
            res[index] = p
        return res