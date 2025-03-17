# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/?envType=daily-question&envId=2025-03-04

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # build powers of three < n/2 / n
        # try perms

        # unoptimised
        # def all_perms(cur, i):
        #     if cur == n:
        #         return True
        #     if cur > n or 3**i > n:
        #         return False
            
        #     if all_perms(cur+3**i, i+1):
        #         return True
        #     return all_perms(cur, i + 1)


        # return all_perms(0,0)

        # optimised - build powers of three, always include max - GREEDY

        threes = [1]
        next_val = 3
        while next_val <= n:
            threes.append(next_val)
            next_val = next_val * 3

        while threes:
            cur = threes.pop()
            if cur <= n:
                n -= cur
            # if n >= cur return False?

            if n == 0:
                return True
        if n == 0 :
            return True
