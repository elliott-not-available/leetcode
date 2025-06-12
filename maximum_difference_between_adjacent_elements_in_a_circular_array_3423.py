# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/?envType=daily-question&envId=2025-06-12

class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        dif = [abs(nums[-1] - nums[0])]

        for i in range(len(nums) - 1):
            dif.append(abs(nums[i] - nums[i+1]))
        return max(dif)