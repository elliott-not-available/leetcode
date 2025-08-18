# https://leetcode.com/problems/range-product-queries-of-powers/description/?envType=daily-question&envId=2025-08-11

from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # generate powers
        # run q
        mod = 10**9 + 7
        pows = []
        cur = 1

        while n > 0:
            if n % 2 == 1:
                pows.append(cur)
            n //=2
            cur *=2

        res = []
        for l, r in queries:
            cur = 1

            for i in range(l, r+1):
                cur = (cur*pows[i]) % mod
            res.append(cur)
        return res