# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/?envType=daily-question&envId=2025-05-27

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # n1 = 0
        # n2 = 0

        # for i in range(n+1):

        #     if i % m == 0:
        #         n2 += i
        #     else:
        #         n1 += i

        # return n1 - n2
        #######################################
        # mathmatical derivation

        # (1 + 2 + 3 + ... + Z) = Z(Z+1)/2
        # sum = 1x + 2x + 3x + ... + kx = (1 + 2 + 3 + ... + k)x = (k(k+1)/2) * x
        n1 = n * (n + 1) // 2
        
        k = n // m
        n2 = k * (k + 1) * m

        return n1 - n2