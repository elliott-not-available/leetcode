# https://leetcode.com/problems/map-of-highest-peak/description/?envType=daily-question&envId=2025-01-22

class Solution_og:
    # super brute force, tree might be better
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        n_rows, n_cols = len(isWater), len(isWater[0])
        res = [[-1]*n_cols for _ in range(n_rows)]

        visited = []

        for i in range(n_rows):
            for j in range(n_cols):
                if isWater[i][j]:
                    res[i][j] = 0
                    visited.append((i, j))

        cur = 0
        nxt = True
        while nxt:
            nxt = False
            for i in range(n_rows):
                for j in range(n_cols):
                    if res[i][j] == cur:
                        if i < n_rows-1 and (i+1, j) not in visited:
                            nxt = True
                            visited.append((i+1, j))
                            res[i+1][j] = cur+1
                        if i > 0 and (i-1, j) not in visited:
                            nxt = True
                            visited.append((i-1, j))
                            res[i-1][j] = cur+1
                        if j < n_cols-1 and (i, j+1) not in visited:
                            nxt = True
                            visited.append((i, j+1))
                            res[i][j+1] = cur+1
                        if j > 0 and (i, j-1) not in visited:
                            nxt = True
                            visited.append((i, j-1))
                            res[i][j-1] = cur+1
            cur += 1
        return res
        
from collections import deque

class Solution:

    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        n_rows, n_cols = len(isWater), len(isWater[0])
        res = [[-1]*n_cols for _ in range(n_rows)] 
        # visited = set()

        q = deque()

        for i in range(n_rows):
            for j in range(n_cols):
                if isWater[i][j]:
                    # visited.add((i, j))
                    res[i][j] = 0
                    q.append((i, j))

        while q:
            r, c = q.popleft()
            h = res[r][c]

            nei = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]

            for nr, nc in nei:
                if (
                    nr < 0 or nc < 0 or
                    nr == n_rows or nc == n_cols or
                    res[nr][nc] != -1
                ):
                    continue

                q.append((nr, nc))
                # visited.add((nr, nc))
                res[nr][nc] = h + 1
        return res





