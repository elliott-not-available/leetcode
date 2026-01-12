# https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-01-12

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        res = 0

        for i in range(1, n):
            pr = points[i-1]
            cr = points[i]

            res += max(abs(pr[0]-cr[0]), abs(pr[1]-cr[1]))
        return res