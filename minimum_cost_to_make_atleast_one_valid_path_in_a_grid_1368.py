# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/?envType=daily-question&envId=2025-01-18

import heapq

class Solution:
    # initial, didnt work, timelimit exceeded on test, some inf loop
    def minCost(self, grid: list[list[int]]) -> int:
        # min heap, add each direction + cost, pop lowest cost, repeat till n * m
        N = len(grid)
        M = len(grid[0])

        visited = [(0,0)]
        min_heap = [(0,0,0)] # [(cost, i, j)]
        def add_moves(cost, i, j):
            if i < N-1 and (i + 1, j) not in visited:
                if grid[i][j] != 1:
                    heapq.heappush(min_heap, [cost + 1, i + 1, j])
                else:
                    heapq.heappush(min_heap, [cost, i + 1, j])

            if i > 0 and (i - 1, j) not in visited:
                # add move left
                if grid[i][j] != 2:
                    heapq.heappush(min_heap, [cost + 1, i - 1, j])
                else:
                    heapq.heappush(min_heap, [cost, i - 1, j])

            if j < M-1 and (i, j + 1) not in visited:
                # add move down
                if grid[i][j] != 3:
                    heapq.heappush(min_heap, [cost + 1, i, j + 1])
                else:
                    heapq.heappush(min_heap, [cost, i, j + 1])

            if j > 0 and (i, j - 1) not in visited:
                # add move up
                if grid[i][j] != 4:
                    heapq.heappush(min_heap, [cost + 1, i, j - 1])
                else:
                    heapq.heappush(min_heap, [cost, i, j - 1])

        while min_heap:
            cost, i, j = heapq.heappop(min_heap)
            if i == N-1 and j == M-1:
                return cost
            add_moves(cost, i, j)

        return -1
    
from collections import deque

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        directions = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1, 0],
        }

        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0)]) # r, c, cost
        min_cost = {(0, 0): 0}

        while q:
            r, c, cost = q.popleft()

            if (r, c) == (ROWS - 1, COLS - 1):
                return cost
            
            for d in directions:
                dr, dc = directions[d]
                nr, nc = r+dr, c+dc
                n_cost = cost if d == grid[r][c] else cost + 1

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or n_cost >= min_cost.get((nr, nc), float("inf")):
                    continue

                min_cost[(nr, nc)] = n_cost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))