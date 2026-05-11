# https://leetcode.com/problems/separate-the-digits-in-an-array/description/?envType=daily-question&envId=2026-05-11

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        for n in nums:
            for c in str(n):
                res.append(int(c))
        
        # return [int(c) for n in nums for c in str(n)]
        return res
            