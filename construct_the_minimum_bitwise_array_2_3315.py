# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description/?envType=daily-question&envId=2026-01-21

class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n

        # brute force is tle
        # for i in range(n):
        #     target = nums[i]
        #     cur = -1

        #     for j in range(target):
        #         if (j | j+1) == target:
        #             cur = j
        #             break
        #     res[i] = cur

        for i in range(n):
            cur = -1
            d = 1
            while (nums[i] & d) != 0:
                cur = nums[i] - d
                d <<= 1
            res[i] = cur

        return res