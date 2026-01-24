# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2026-01-24

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) // 2):
            res = max(res, nums[i] + nums[-i-1])
        return res