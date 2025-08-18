# https://leetcode.com/problems/rearranging-fruits/description/?envType=daily-question&envId=2025-08-02
from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c = Counter(basket1)
        m = min(c)

        for b2 in basket2:
            c[b2] -= 1
            m=min(m, b2)

        mg = []

        for n, cnt in c.items():
            if cnt % 2 != 0:
                return -1
            mg.extend([n] * (abs(cnt) // 2))

        if not mg:
            return 0
        mg.sort()
        return sum(min(2*m, x) for x in mg[:len(mg) // 2])