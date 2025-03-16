# https://leetcode.com/problems/minimum-time-to-repair-cars/description/?envType=daily-question&envId=2025-03-16
from math import sqrt

class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:

        # binary search - didnt figure it out myself

        l = 1
        r = max(ranks) * (cars ** 2)
        res = -1

        def count_repaired(time):
            tot = 0
            for r in ranks:
                tot += int(sqrt(time / r))
            return tot

        while l <= r:
            m = (l+r) // 2
            repaired = count_repaired(m)

            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
        