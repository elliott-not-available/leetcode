# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/?envType=daily-question&envId=2026-04-19

class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        
        n = len(nums1)
        # mj = max(nums2)
        # res = 0

        # for i in range(n):
        #     if nums1[i] > mj:
        #         continue

        #     for j in range(i, n):
        #         if nums1[i] > nums2[j]:
        #             continue

        #         res = max(res, j-i)

        # return res

        i=0
        j=0

        while i <n and j<n:
            i+= nums1[i]>nums2[j]
            j+= 1
        return max(0, j-i-1)