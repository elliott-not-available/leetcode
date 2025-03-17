# minimum_array_end_3133
# https://leetcode.com/problems/minimum-array-end/description/?envType=daily-question&envId=2024-11-09

class Solution_og:
    def minEnd(self, n: int, x: int) -> int:
        # timeout fail
        # neeted
        # output array starts with x
        # every int in the output array must have all the same set bits as x
        res = x
        for _ in range(n-1):
            res += 1
            # bitwise or
            res = res | x

        return res
    
class Solution:
    def minEnd(self, n: int, x:int) -> int:
        # neeted
        res = x
        i_x = 1 
        i_n = 1 

        while i_n < n:

            if i_x & x == 0:
                if i_n & (n-1):
                    res = res | i_x

                i_n = i_n << 1
            i_x = i_x << 1
        
        return res