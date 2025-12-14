# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2025-12-14

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # # top down dp, only just passes
        # mod = 10**9 + 7
        
        # cache = [[-1]*3 for _ in range(len(corridor))]

        # def count(index, seats):
        #     if index == len(corridor):
        #         return 1 if seats == 2 else 0
            
        #     if cache[index][seats] != -1:
        #         return cache[index][seats]
            
        #     if seats == 2:
        #         if corridor[index] == "S":
        #             res = count(index+1, 1)
        #         else:
        #             res = (count(index+1, 0) + count(index+1, 2)) % mod
        #     else:
        #         if corridor[index] == "S":
        #             res = count(index+1, seats+1)
        #         else:
        #             res = count(index+1, seats)
        #     cache[index][seats]  = res
        #     return cache[index][seats]
        # return count(0, 0)

        # Space-Optimized Bottom-up Dynamic Programming
        mod = 10**9 + 7

        zero = 0
        one = 0
        two = 1

        # me no understand

        for item in corridor:
            if item == "S":
                zero = one
                one, two = two, one
            else:
                two = (two+zero) % mod

        return zero