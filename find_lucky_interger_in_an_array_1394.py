# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/?envType=daily-question&envId=2025-07-05
from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        res = -1
        for k,v in Counter(arr).items():
            if k == v:
                res = max(res, k)
        return res

        