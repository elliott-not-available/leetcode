# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/?envType=daily-question&envId=2025-11-23

class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:

        mod_0 = [n for n in nums if n%3==0]
        mod_1 = sorted([n for n in nums if n%3==1], reverse=True)
        mod_2 = sorted([n for n in nums if n%3==2], reverse=True)
        n_1 = len(mod_1)
        n_2 = len(mod_2)

        res = 0

        for x in [n_1 - 2, n_1 - 1, n_1]:
            if x >= 0:

                for y in [n_2 -2, n_2 -1, n_2]:
                    if y >=0 and (x-y)%3 == 0:
                        res = max(res, sum(mod_1[:x]) + sum(mod_2[:y]))
        return res + sum(mod_0)
        