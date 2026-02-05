# https://leetcode.com/problems/transformed-array/?envType=daily-question&envId=2026-02-05

class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        res = [0] * n

        for i in range(n):
            new_index = (i + nums[i]) % n
            res[i] = nums[new_index]

        return res