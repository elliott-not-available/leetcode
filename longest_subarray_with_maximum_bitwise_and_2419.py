# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2025-07-30
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 0
        cur = 0
        res = 0

        for n in nums:
            if mx < n:
                mx = n
                cur = 0
                res = 0

            if mx == n:
                cur += 1
            else:
                cur = 0

            res = max(res, cur)
        return res