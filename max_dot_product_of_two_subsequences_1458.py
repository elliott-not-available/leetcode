# https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/?envType=daily-question&envId=2026-01-08

class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:

        n, m = len(nums1), len(nums2)
        
        if m > n:
            return self.maxDotProduct(nums2, nums1)
        minmin = 1000 * 1000 * -1
        dp = [minmin] * (m+1)

        for i in range(1, n+1):
            pre = minmin

            for j in range(1, m+1):
                cur = nums1[i-1] * nums2[j-1]
                tmp = dp[j]

                dp[j] = max(cur, cur+pre, dp[j], dp[j-1])
                pre = tmp
        return dp[m]