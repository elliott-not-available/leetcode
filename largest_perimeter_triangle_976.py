# https://leetcode.com/problems/largest-perimeter-triangle/?envType=daily-question&envId=2025-09-28


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums)-3, -1, -1):
            if nums[i]+nums[i+1] > nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0