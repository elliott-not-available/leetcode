# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/?envType=daily-question&envId=2025-07-04

class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        res = 0

        while k != 1:
            t = k.bit_length() - 1
            if (1 <<t) == k:
                t -=1
            k -=1 << t
            if operations[t]:
                res += 1
        return chr(ord("a") + (res % 26))