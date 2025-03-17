# https://leetcode.com/problems/minimum-length-of-string-after-operations/description/?envType=daily-question&envId=2025-01-13

from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        string_counter = Counter(s)
        res = len(s)
        for _, v in string_counter.items():
            while v > 2:
                v -= 2
                res -= 2
        return res