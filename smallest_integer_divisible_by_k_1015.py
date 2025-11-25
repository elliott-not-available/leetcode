# https://leetcode.com/problems/smallest-integer-divisible-by-k/?envType=daily-question&envId=2025-11-25

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0: return -1
        # n can only contain 1  
        # n%k == 0

        rem = 0

        for l in range(1, k+1):
            rem = (rem*10+1) % k
            if rem == 0:
                return l
        return -1