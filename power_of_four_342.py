# https://leetcode.com/problems/power-of-four/description/?envType=daily-question&envId=2025-08-15

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # some wierd binary stuff in the solution
        if n == 1:
            return True
        if n % 4:
            return False

        cur = 1
        while cur <= n:

            if cur == n:
                return True
            cur *= 4
        return False
