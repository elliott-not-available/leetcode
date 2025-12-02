# https://leetcode.com/problems/count-number-of-trapezoids-i/description/?envType=daily-question&envId=2025-12-02
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: list[ list[int]]) -> int:
        y_points = defaultdict(int)

        for p in points:
            y_points[p[1]] += 1

        # number of lines = y_point*(y_point-1) // 2
        res = 0
        tot = 0
        MOD = 10**9 + 7
        for y in y_points.values():
            lins = y*(y-1) //2
            res = (res + lins*tot) % MOD
            tot = (tot + lins) % MOD


        return res