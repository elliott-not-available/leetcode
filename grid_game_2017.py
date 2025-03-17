# https://leetcode.com/problems/grid-game/description/?envType=daily-question&envId=2025-01-21

class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        N = len(grid[0])
        pre1 = [0]*N
        pre2 = [0]*N

        pre1[0] = grid[0][0]
        pre2[0] = grid[1][0]
        for i in range(1, N):
            pre1[i] = pre1[i-1] + grid[0][i]
            pre2[i] = pre2[i-1] + grid[1][i]

        res = float("inf")
        for i in range(N):
            top = pre1[-1] - pre1[i]
            bot = pre2[i-1] if i > 0 else 0
            second_rob = max(top, bot)
            res = min(res, second_rob)

        return res