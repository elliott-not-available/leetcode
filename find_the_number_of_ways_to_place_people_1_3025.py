# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description/?envType=daily-question&envId=2025-09-02

from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        n = len(points)
        res = 0

        for i in range(n):
            for j in range(n):
                if i == j: continue

                a = points[i]
                b = points[j]

                if not (a[0] <= b[0] and a[1] >= b[1]): continue

                if n == 2:
                    res += 1
                    continue
                
                contains = False
                for k in range(n):
                    if k==i or k==j: continue

                    tmp = points[k]

                    xcontains = (tmp[0] >= a[0] and tmp[0] <= b[0])
                    ycontains = (tmp[1] <= a[1] and tmp[1] >= b[1])

                    if xcontains and ycontains:
                        contains = True
                        break

                if not contains:
                    res += 1







        return res