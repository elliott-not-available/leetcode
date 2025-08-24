# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=daily-question&envId=2025-08-24

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        # find longest adjacent pair of 1-substrings?

        pre, cur = 0,0
        res = 0

        for n in nums:

            if n == 1:
                cur += 1

            if n == 0:
                res = max(res, pre+cur)
                pre = cur
                cur = 0

        res = max(res, pre+cur)
        if res == len(nums):
            res -= 1

        return res
        