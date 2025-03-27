# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2025-03-26

class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:

        # check if possible with mod/remainder
        prev_mod = grid[0][0] % x
        grid_list = []
        total = 0
        for n in grid:
            for m in n:
                cur_mod = m % x
                grid_list.append(m)
                total += m

                if cur_mod != prev_mod:
                    return -1
                
        # create sorted list,
        grid_list.sort()

        # prefix sum?
        prefix = 0
        res = float("inf")

        for i in range(len(grid_list)):
            cost_left = grid_list[i]*i - prefix
            cost_right = total - prefix - (grid_list[i] * (len(grid_list) - i))
            ops = (cost_left + cost_right) // x

            res = min(res, ops)

            prefix += grid_list[i]

        return res
        