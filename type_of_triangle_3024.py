# https://leetcode.com/problems/type-of-triangle/description/?envType=daily-question&envId=2025-05-19
from collections import defaultdict

class Solution:
    def triangleType(self, nums: list[int]) -> str:

        traingle_type = {
            1: "scalene",
            2: "isosceles",
            3: "equilateral",
        }

        mm = 0
        m = defaultdict(int)

        for n in nums:
            m[n] += 1
            mm = max(mm, m[n])

        # check it can form a triangle
        tot = sum(nums)

        for n in nums:
            # if one side is greaster than sum of 2 sides
            if n >= tot-n:
                return "none"

        return traingle_type[mm]
        