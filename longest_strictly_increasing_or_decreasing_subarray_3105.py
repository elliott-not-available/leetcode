# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        ups = 1
        downs = 1
        max_l = 1
        pre = nums[0]

        for i in range(1,len(nums)):
            if pre < nums[i]:
                ups += 1
                downs = 1
                max_l = max(max_l, ups)
            elif pre > nums[i]:
                downs += 1
                ups = 1
                max_l = max(max_l, downs)
            else:
                ups = 1
                downs = 1
            pre = nums[i]


        return max_l
        