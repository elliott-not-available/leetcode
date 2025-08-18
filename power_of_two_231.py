# https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2025-08-09

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # there is a oneline binary comparison solution (more efficition in space and time)
        
        i = 0
        cur = 0
        while cur < n:
            cur = 2**i
            if cur == n:
                return True
            else:
                i += 1
        return False
        