# https://leetcode.com/problems/count-servers-that-communicate/description/?envType=daily-question&envId=2025-01-23

class Solution_wrong:
    # this is a solution for a different problem - the question was asking SAME ROW OR COLUMN not adjacent
    def countServers(self, grid: list[list[int]]) -> int:
        # travers throu grid
        # if location neighbours contain 1 then res +1 (+ visited)

        # could do something greedy here -> follow the +1 and add to visited
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 1 and grid[i][j] not in visited:

                    nei = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]

                    for nr, nc in nei:

                        if (
                            (nr, nc) in visited or
                            nr < 0 or nc < 0 or
                            nr == ROWS or nc == COLS or
                            grid[nr][nc] != 1
                        ):
                            continue

                        visited.add((nr, nc))
                        res += 1
                visited.add((i, j))
        return res
    
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    if row_cnt[r] > 1 or col_cnt[c] > 1:
                        res += 1

        return res
        