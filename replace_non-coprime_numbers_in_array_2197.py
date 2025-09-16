# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description/?envType=daily-question&envId=2025-09-16
from math import gcd, lcm
class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        res = []

        cur = nums[0]

        for n in nums[1:]:
            if gcd(cur, n) > 1:
                cur = lcm(cur, n)

                while res and gcd(cur, res[-1]) > 1:
                    cur = lcm(cur, res.pop())
            else:
                res.append(cur)
                cur = n

        res.append(cur)

        return res