# https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18class Solution:
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        bin_n = bin(n)[2:]

        for i in range(1, len(bin_n)):
            if bin_n[i]==bin_n[i-1]:
                return False

        return True