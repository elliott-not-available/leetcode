# https://leetcode.com/problems/closest-prime-numbers-in-range/description/?envType=daily-question&envId=2025-03-07

from math import sqrt

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        # the fastest solution uses composite witness and miller_rabin


        # find all primes starting after left and upto right_n and keep list
        # iterate from left to right, getting the min diff between 2 values
        # if diff < min diff: res[0] = i, res[1] = j

        # # My bruteforce solution (slightly optimised), gets timelimit exceeded
        # primes = [2,3]
        # def is_prime(i: int) -> bool:
        #     lmt = sqrt(i)
        #     index = 0
        #     cur = primes[index]

        #     while cur <= lmt:
        #         if i % cur == 0:
        #             # print(f"{cur} divides {i}")
        #             return False
        #         index += 1
        #         cur = primes[index]
        #     return True

        # pairs = []
        # if left == 3 and right > 3:
        #     pairs.append(3)
        # if (left == 2 and right > 2) or (left == 1 and right > 2):
        #     pairs.append(2)
        #     pairs.append(3)

        # for i in range(4, right+1):
        #     # check if prime
        #     # print(f"checking {i}")
        #     if is_prime(i):
        #         # print(f"adding {i} to primes")
        #         primes.append(i)
        #         if i >= left:
        #             # print(f"adding {i} to pairs")
        #             pairs.append(i)          


        if right - left < 1:
            return [-1, -1]
        if left <= 2 and right >= 3:
            return [2,3]

        # sieve of eratosthenes - probs need to memorise

        def get_primes():
            is_prime = [True] * (right + 1)
            is_prime[0] = False
            is_prime[1] = False

            for n in range(2, int(sqrt(right))+1):
                if not is_prime[n]:
                    continue
                for m in range(n + n, right + 1, n):
                    is_prime[m] = False

            primes = []

            for i in range(len(is_prime)):
                if is_prime[i] and i >= left:
                    primes.append(i)
            return primes

        pairs = get_primes()
        min_dif = float("inf")
        res = [-1, -1]

        print(pairs)

        for i in range(len(pairs)-1):
            j = i+1
            if pairs[j] - pairs[i] < min_dif:
                # print(f"{pairs[j]} - {pairs[i]} < {min_dif}")
                min_dif = pairs[j] - pairs[i]
                res = [pairs[i], pairs[j]]

        return res
