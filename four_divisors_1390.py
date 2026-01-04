# https://leetcode.com/problems/four-divisors/?envType=daily-question&envId=2026-01-04

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        # APPARANTLY:

        # A number has exactly 4 divisors if and only if it is one of these two forms:
        # Case 1: p^3
        # Case 2: p×q (Where p and q are two distinct primes)

        res = 0

        for n in nums:
            cnt = 0
            sm = 0
            root = int(n**0.5)

            for i in range(1, root + 1):
                if n % i ==0:
                    j = n // i
                    if i ==j:
                        cnt += 1
                        sm += i
                    else:
                        cnt += 2
                        sm += i+j
                    
                    if cnt > 4:
                        break
            
            if cnt == 4:
                res += sm



        return res
        