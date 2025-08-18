# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description/?envType=daily-question&envId=2025-08-03

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # sliding window? nein you start at start and move l/r
        # actually you could do some sliding window stuff

        n = len(fruits)
        sums = [0] * (n+1)
        inds = [0] * n
        res = 0

        for i in range(n):
            sums[i+1] = sums[i] + fruits[i][1]
            inds[i] = fruits[i][0]

        for x in range(k // 2 + 1):

            y = k - 2*x
            l1 = startPos - x
            r1 = startPos + y

            l2 = startPos - y
            r2 = startPos + x

            start1 = bisect_left(inds, l1)
            end1 = bisect_right(inds, r1)

            start2 = bisect_left(inds, l2)
            end2 = bisect_right(inds, r2)

            res = max(res, sums[end1]-sums[start1], sums[end2] - sums[start2])

        return res