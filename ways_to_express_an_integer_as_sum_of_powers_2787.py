# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/?envType=daily-question&envId=2025-08-12

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        mod = 10**9 + 7

        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            cur = i**x

            if cur > n:
                break
            for j in range(n, cur-1, -1):
                dp[j] = (dp[j] + dp[j-cur]) % mod
        return dp[n]