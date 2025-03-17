# https://leetcode.com/problems/first-completely-painted-row-or-column/description/?envType=daily-question&envId=2025-01-20
from collections import defaultdict

class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        col_max = len(mat)
        row_max = len(mat[0])
        hm = {}
        for i in range(col_max):
            for j in range(row_max):
                hm[mat[i][j]] = (i, j)

        row_count = defaultdict(int)
        col_count = defaultdict(int)

        for i, a in enumerate(arr):
            r, c = hm[a]
            row_count[r] += 1
            col_count[c] += 1

            if row_count[r] == row_max or col_count[c] == col_max:
                return i

        