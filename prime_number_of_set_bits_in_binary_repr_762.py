# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/?envType=daily-question&envId=2026-02-21

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        p_max = 13
        
        def is_prime(num):
            if num > p_max:
                print(f"{num} is larger than max: {p_max}")
            if num in primes:
                return 1
            return 0
        
        res = 0

        for i in range(left, right+1):
            bin_repr = bin(i)[2:]
            res += is_prime(bin_repr.count("1"))

        return res