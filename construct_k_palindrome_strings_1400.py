# https://leetcode.com/problems/construct-k-palindrome-strings/?envType=daily-question&envId=2025-01-11
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        l = Counter(s)
        odd = 0

        for cnt in l.values():
            odd += cnt % 2

        return odd <= k
