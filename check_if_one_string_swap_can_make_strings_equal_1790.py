# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/?envType=daily-question&envId=2025-02-05

from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if Counter(s1) != Counter(s2):
            return False

        count = 0

        for i in range(len(s1)):
            if count > 2:
                return False
            if s1[i] != s2[i]:
                count += 1

        return count <= 2