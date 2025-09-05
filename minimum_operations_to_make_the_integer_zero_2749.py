# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/?envType=daily-question&envId=2025-09-05

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # operation : num1 - ((2**i) + num2)
        # 0 <= i <= 60

        for k in range(1, 61):
            x = num1 - num2*k

            if x < k:
                return -1
            
            if k >= x.bit_count():
                return k
            
        return -1