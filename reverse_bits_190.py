# https://leetcode.com/problems/reverse-bits/description/?envType=daily-question&envId=2026-02-16class Solution:
class Solution:
    def reverseBits(self, n: int) -> int:

        res = ["0"]*32
        bin_n = bin(n)[2:]
        length = len(bin_n)
        rem = 32 - length

        for i in range(length):
            if bin_n[i] == "1":
                res[-i-rem-1] = "1"

             
        return int("".join(res),2)