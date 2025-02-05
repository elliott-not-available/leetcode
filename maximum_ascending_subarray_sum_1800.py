# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04

class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cur_sum += nums[i+1]
            else:
                cur_sum = nums[i+1]
            max_sum = max(max_sum, cur_sum)

        return max_sum
        