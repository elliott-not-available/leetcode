#https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2025-11-02

class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        # brute force simulation
        mapa = [[False]*n for _ in range(m)]

        for g in guards:
            mapa[g[0]][g[1]] = "G"

        for w in walls:
            mapa[w[0]][w[1]] = "W"

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        for g in guards:
            row, col = g
            for dr, dc in dirs:

                n_row = row + dr
                n_col = col + dc


                while 0 <= n_row < m and 0 <= n_col < n:

                    if mapa[n_row][n_col] in ["W", "G"]:
                        break

                    mapa[n_row][n_col] = "r"
                    n_row = n_row + dr
                    n_col = n_col + dc
        print(mapa)

        empty_spaces = 0
        for row in mapa:
            empty_spaces += row.count(False)

        return empty_spaces 
    

