# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solutions/7482069/simple-lcs-finding-by-sumeet_sharma-1-kcva/?envType=daily-question&envId=2026-01-10class Solution:
    
class Solution:

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        tot = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return tot -2*dp[n][m]