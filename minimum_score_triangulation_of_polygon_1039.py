# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/?envType=daily-question&envId=2025-09-29
from functools import lru_cache

class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        # values.sort()
        # print(values)
        # return values[0] * values[1] * values[2]

        # dont really understand what is being asked
        # ye dont understand fudge

        @lru_cache(None)
        def dp(i, j):
            if i + 2 > j:
                return 0
            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]
            return min(
                (values[i] * values[k] * values[j] + dp(i, k) + dp(k, j))
                for k in range(i + 1, j)
            )

        return dp(0, len(values) - 1)

