# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17

class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0

        for n in nums:
            n %= k

            for pre in range(k):
                dp[pre][n] = dp[n][pre] + 1

                res = max(res, dp[pre][n])
        return res