# https://leetcode.com/problems/special-positions-in-a-binary-matrix/?envType=daily-question&envId=2026-03-04

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:

        rows = len(mat)
        cols = len(mat[0])

        row_count = [0]*rows
        col_count = [0]* cols
        res = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==1:
                    row_count[r] += 1
                    col_count[c] += 1

        for row in range(rows):
            if row_count[row]==1:
                    
                for col in range(cols):
                    if mat[row][col]==1 and col_count[col]==1:
                        
                        res += 1

        # for i in range(rows):
        #     for j in range(cols):

        #         if mat[i][j] == 1:
        #             if sum(mat[i])==1 and sum(mat[k][j] for k in range(rows))==1:
        #                 res += 1
        #                 # skip to next i

        return res