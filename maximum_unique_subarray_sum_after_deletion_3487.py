# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=daily-question&envId=2025-07-25

class Solution:
    def maxSum(self, nums: list[int]) -> int:
        
        good = set([n for n in nums if n > 0])

        if len(good) == 0:
            return max(nums)
        
        return sum(good)