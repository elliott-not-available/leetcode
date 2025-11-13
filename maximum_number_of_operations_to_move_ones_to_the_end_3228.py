# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/?envType=daily-question&envId=2025-11-13

class Solution:
    def maxOperations(self, s: str) -> int:
        # simulation

        n = len(s)
        res = 0
        c = 0
        i = 0

        while i < n:
            if s[i] == "0":
                while i+1 < n and s[i+1] == "0":
                    i += 1
                res += c
            else:
                c += 1
            i += 1

        return res