# https://leetcode.com/problems/build-array-from-permutation/description/?envType=daily-question&envId=2025-05-06

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]