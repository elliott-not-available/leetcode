# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/?envType=daily-question&envId=2026-01-20

class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            t = nums[i]
            cur = -1

            for j in range(t):

                # if too big -> set to -1
                # if (j | j + 1) > t:
                #     cur = -1
                    # break
                    
                # if it matches set cur to j and early break
                if (j | j + 1) == t:
                    cur = j
                    # res[i] = j
                    break
            res[i] = cur

        return res