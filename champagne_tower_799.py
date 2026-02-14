# https://leetcode.com/problems/champagne-tower/?envType=daily-question&envId=2026-02-14




class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        # overflow is not equal

        tower = [[0]*100 for _ in range(100)]
        tower[0][0] = poured

        for i in range(query_row+1):
            for j in range(i+1):
                if tower[i][j] > 1:
                    half_overflow = (tower[i][j] - 1) / 2
                    tower[i][j] = 1
                    tower[i+1][j] += half_overflow
                    tower[i+1][j+1] += half_overflow
        

        return tower[query_row][query_glass]