# https://leetcode.com/problems/count-square-submatrices-with-all-ones/editorial/?envType=daily-question&envId=2025-08-20
from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r, c  = len(matrix), len(matrix[0])
        dp = [[0] * (c+1) for _ in range(r+1)]

        res = 0

        for i in range(r):
            for j in range(c):
                if matrix[i][j]:
                    dp[i+1][j+1] = (
                        min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    )
                    res += dp[i+1][j+1]
        return res