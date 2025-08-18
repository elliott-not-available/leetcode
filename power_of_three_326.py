# https://leetcode.com/problems/power-of-three/description/?envType=daily-question&envId=2025-08-13

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # this solutions is as inefficent as it gets
        cur = 1

        while cur <= n:
            print(cur)
            if cur == n:
                return True
            
            cur *= 3
            
        return False


