# https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2026-03-08

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        # Cantor's Diagonal Argument editorial solution looks cool
        n = len(nums[0])
        c = 2 ** n

        for i in range(c):
            # transl = "{:0nd}".format(bin(i)[2:])
            transl = bin(i)[2:].zfill(n)
            if transl not in nums:
                return transl


        return False
         