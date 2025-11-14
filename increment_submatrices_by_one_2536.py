# https://leetcode.com/problems/increment-submatrices-by-one/description/?envType=daily-question&envId=2025-11-14

class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:

        # # simulation - timelimit exceeded
        # res = [[0]*n for _ in range(n)]
        # for start_r, start_c, end_r, end_c in queries:

        #     for r in range(start_r, end_r+1):
        #         for c in range(start_c, end_c+1):
        #             res[r][c] += 1
        
        # return res

        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r2 + 1][c1] -= 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                above = mat[i - 1][j] if i > 0 else 0
                left = mat[i][j - 1] if j > 0 else 0
                diag = mat[i - 1][j - 1] if i > 0 and j > 0 else 0
                mat[i][j] = diff[i][j] + above + left - diag
        return mat