# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/?envType=daily-question&envId=2025-10-16
from collections import Counter
class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        remainder = Counter(n % value for n in nums)
        print(remainder)

        res = 0

        # for i in range(value+1):
        #     if remainder[i] == 0:
        #         return i
        # return False

        while remainder[res % value] > 0:
            remainder[res % value] -= 1
            res += 1
        return res