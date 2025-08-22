# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/?envType=daily-question&envId=2025-08-22
from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # find max 1 for l,r, t,b? - even tho its 1 pass, seems about maximum inefficient
        rows, cols = len(grid), len(grid[0])

        left, right, bot, top = cols, 0, 0, rows


        # def update_stuff(vert, hori, left, right, bot, top):
        #     top = min(vert, top)
        #     bot = max(vert, bot)

        #     left = min(left, hori)
        #     right = max(right, hori)
        #     return left, right, bot, top
        

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    # left, right, bot, top = update_stuff(i,j, left, right, bot, top)
                        top = min(i, top)
                        bot = max(i, bot)

                        left = min(left, j)
                        right = max(right, j)
        
        res = (right - left + 1) * (bot - top + 1)


        return res