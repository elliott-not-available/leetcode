# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/?envType=daily-question&envId=2025-08-26

from typing import List
from math import sqrt

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        cur_max = 0

        for r in dimensions:

            cur_dia = sqrt(r[0]**2 + r[1]**2)

            if cur_dia > cur_max:
                res = r[0] * r[1]
                cur_max = cur_dia
        
        return res