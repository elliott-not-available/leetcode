# https://leetcode.com/problems/last-day-where-you-can-still-cross/?envType=daily-question&envId=2025-12-31
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:

        def can_cross(day):
            grid = [[0] * col for _ in range(row)]

            for i in range(day):
                r,c = cells[i][0] - 1, cells[i][1] - 1
                grid[r][c] = 1

            q = deque()
            visited = [[False] * col for _ in range(row)]
            
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0,c))
                    visited[0][c] = True

            cards = [(1,0), (0, 1), (-1,0), (0,-1)]

            while q:
                r,c = q.popleft()

                if r == row-1:
                    return True
                
                for dr, dc in cards:
                    nr,nc = r + dr, c + dc

                    if 0<=nr<row and 0<=nc<col and not visited[nr][nc] and grid[nr][nc]==0:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            return False
        
        left, right = 1, len(cells)
        res = 0

        while left <= right:
            m = (left+right)//2

            if can_cross(m):
                res = m
                left = m+1
            else:
                right = m-1

        return res