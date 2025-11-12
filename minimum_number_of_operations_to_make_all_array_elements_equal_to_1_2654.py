# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/?envType=daily-question&envId=2025-11-12
from math import gcd
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ones = 0
        g = 0

        for x in nums:
            if x == 1:
                ones += 1
            g = gcd(g, x)

        if ones:
            return n - ones
        if g > 1:
            return -1
        
        min_len = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return min_len + n - 2