# https://leetcode.com/problems/trapping-rain-water-ii/?envType=daily-question&envId=2025-01-19

from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])

        # add border, mark as visited
        min_heap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS-1] or c in [0, COLS-1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1 # mark visit

        # proitise smallest
        # Maintain max height to calc
        # water stored in each inner pos

        res = 0
        max_h = -1

        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h

            neighbs = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in neighbs:
                if (
                    nr < 0 or nc < 0 or
                    nr == ROWS or nc == COLS or
                    heightMap[nr][nc] == -1
                ):
                    continue
                heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1

        return res