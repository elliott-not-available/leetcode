# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=daily-question&envId=2025-07-27
from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        l = 0

        for i in range(1, len(nums) -1):
            # skip duplicates
            if nums[i] != nums[i+1]:
                if (nums[i] > nums[l] and nums[i] > nums[i+1]) or (nums[i] < nums[l] and nums[i] < nums[i+1]):
                    res += 1
                l = i
        return res