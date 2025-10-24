# https://leetcode.com/problems/next-greater-numerically-balanced-number/?envType=daily-question&envId=2025-10-24
from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def check(n):
            c = Counter(str(n))
            for k in c.keys():
                if int(k) != c[k]:
                    return False
            return True

        while n < 10**6 + 1:
            n += 1
            if check(n):
                return n

        return False