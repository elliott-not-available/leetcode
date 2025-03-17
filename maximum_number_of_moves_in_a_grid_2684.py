# maximum_number_of_moves_in_a_grid_2684
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:

        rows, columns = len(grid), len(grid[0])
        res_map = {}

        def dfs(i, j, moves):
            nonlocal grid, rows, columns

            temp_max1 = 0
            temp_max2 = 0
            temp_max3 = 0

            if ((i-1) >= 0 and (j+1) < columns) and grid[i-1][j+1] > grid[i][j]:
                # print(f"up-right {i} {j} valid")
                if (i-1, j+1) not in res_map:
                    res_map[(i-1, j+1)] = dfs(i-1, j+1, moves+1)
                temp_max1 = res_map[(i-1, j+1)]

            if (j+1) < columns and grid[i][j+1] > grid[i][j]:
                # print(f"right {i} {j} valid")
                if (i, j+1) not in res_map:
                    res_map[(i, j+1)] = dfs(i, j+1, moves+1)
                temp_max2 = res_map[(i, j+1)]


            if ((i+1) < rows and (j+1) < columns) and grid[i+1][j+1] > grid[i][j]:
                # print(f"down-right {i} {j} valid")
                if (i+1, j+1) not in res_map:
                    res_map[(i+1, j+1)] = dfs(i+1, j+1, moves+1)
                temp_max3 = res_map[(i+1, j+1)]

            return max(moves, temp_max1, temp_max2, temp_max3)


        return max([dfs(r, 0, 0) for r in range(rows)])
        
        # m x n matrix (m = rows, n = columns)
        # m * 3n (but all 3n work is repeated work) = m * n