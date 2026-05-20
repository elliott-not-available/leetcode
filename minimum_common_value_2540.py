# https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2026-05-19

class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        
        for n1 in nums1:
            if n1 in nums2:
                return n1
        return -1