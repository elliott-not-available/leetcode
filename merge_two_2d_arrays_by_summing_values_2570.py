# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=daily-question&envId=2025-03-02

class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:

        data = {}

        for numl in [nums1, nums2]:
            for i in range(len(numl)):
                n1 = numl[i]
   
                if n1[0] not in data:
                    data[n1[0]] = n1[1]
                else:
                    data[n1[0]] += n1[1]

        keys = sorted(data.keys())

        res = [[key, data[key]] for key in keys]
        return res
        