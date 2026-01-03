# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/?envType=daily-question&envId=2026-01-03

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        pat1, pat2 = 6, 6

        for _ in range(2, n+1):
            pat1, pat2 = (3*pat1 + 2*pat2) % MOD, (2*pat1 + 2*pat2) % MOD
        return (pat1 + pat2) % MOD