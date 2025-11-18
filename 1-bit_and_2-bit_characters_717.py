# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/?envType=daily-question&envId=2025-11-18

class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n-1:
            i += bits[i] + 1
        res = (i==n-1)
        return res