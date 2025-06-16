# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/?envType=daily-question&envId=2025-06-16

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:

        # brute force
        # n = len(nums)
        # res = -1
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] > nums[j]:
        #             continue
        #         res = max(res, nums[j]-nums[i])
        # return res
        ############################################
        # prefix min value
        n = len(nums)
        res, premin = -1, nums[0]

        for i in range(1, n):
            if nums[i] > premin:
                res = max(res, nums[i] - premin)
            else:
                premin = nums[i]

        return res