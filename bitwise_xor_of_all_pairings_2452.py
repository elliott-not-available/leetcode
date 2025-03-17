# https://leetcode.com/problems/bitwise-xor-of-all-pairings/?envType=daily-question&envId=2025-01-16

class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        res = 0

        if len(nums2) % 2 == 1:
            for n in nums1:
                res ^= n

        if len(nums1) % 2 == 1:
            for n in nums2:
                res ^= n

        return res