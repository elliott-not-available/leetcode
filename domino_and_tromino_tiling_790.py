# https://leetcode.com/problems/domino-and-tromino-tiling/description/?envType=daily-question&envId=2025-05-05

class Solution:
    def numTilings(self, n: int) -> int:
        # recursion or math
        MOD = 10**9 + 7
        # recursion: timelimit exceeded

        # def rec(i, n, possible):
        #     if i == n: return 0 if possible else 1
        #     if i > n: return 0

        #     if possible:
        #         return (rec(i+1, n, False) + rec(i+1, n, True)) % MOD
        #     return (rec(i+1, n, False) + rec(i+2, n, False) + 2*rec(i+2, n, True)) % MOD
        # return rec(0, n, False)
        #############################################
        # # math:
        if n <= 1: return 1
        if n == 2: return 2
        if n == 3: return 5

        dp = [0] * (n+1)
        dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 5

        for i in range(4, n+1):
            dp[i] = (dp[i-1]*2 + dp[i-3]) % MOD
        return dp[n]