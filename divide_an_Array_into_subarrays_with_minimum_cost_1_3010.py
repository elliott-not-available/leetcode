# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/?envType=daily-question&envId=2026-02-01

class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        res = nums[0]
        rest = sorted(nums[1:])
        res += rest[0] + rest[1]
        return res