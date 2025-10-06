# https://leetcode.com/problems/swim-in-rising-water/description/?envType=daily-question&envId=2025-10-06
import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        n = len(grid)
        seen = [[False]*n for _ in range(n)]
        max_time = 0
        minheap = [(grid[0][0], 0, 0)] # value row col
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        while minheap:
            cur_height, row, col = heapq.heappop(minheap)
            print(f"{cur_height}, {row}, {col}")

            if seen[row][col]:
                continue
            seen[row][col] = True
            max_time = max(max_time, cur_height)

            if row == n-1 and col == n-1:
                return max_time
            
            for dx, dy in dirs:
                x, y = row + dx, col+dy

                if 0 <= x < n and 0 <= y < n and not seen[x][y]:
                    heapq.heappush(minheap, (grid[x][y], x, y))
            

        return max_time