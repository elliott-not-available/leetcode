# prime_subtraction_operation_2601
# https://leetcode.com/problems/prime-subtraction-operation/description/?envType=daily-question&envId=2024-11-11
import math

class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        max_n = max(nums)

        def get_primes(max_n: int) -> list[int]:
            primes = [2]
            for i in range(2, max_n):
                skip = False
                for j in range(2, math.ceil(math.sqrt(i)) + 1):
                    if i % j == 0:
                        skip = True
                        break

                if not skip:
                    primes.append(i)
                
            return primes
        
        primes = get_primes(max_n)
        print(f"PRIMES: {primes}")
        pre = 0

        nums_copy = nums.copy()

        for i in range(len(nums_copy)):

            for p in reversed(primes):
                if p < nums_copy[i] and pre < nums_copy[i]-p:
                    nums_copy[i] = nums_copy[i] - p

                    break

            

            if nums_copy[i] <= pre:
                print(nums_copy)
                print(nums_copy[i], pre)
                return False

            pre = nums_copy[i]

        print(nums_copy)
        return True
    

class Solution_neet:
    # NEETED
    def primeSubOperation(self, nums: list[int]) -> bool:
        def is_prime(n):
            for f in range(2, int(math.sqrt(n)) + 1):
                if n % f == 0:
                    return False
            return True
        
        primes = [0, 0]

        for i in range(2, max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i-1])

        prev = 0

        for n in nums:
            upper = n - prev
            largest_p = primes[upper -1]

            if n- largest_p <= prev:
                return False
            prev = n - largest_p
        return True