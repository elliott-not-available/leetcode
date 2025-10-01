# https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2025-10-01

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        # total = 0
        # def rec(inp, total):

        #     if inp<numExchange:
        #         print(f"end: {total} + {inp}")
        #         return total + inp
        #     else:
        #         total += inp
        #         print(f"adding: {total-inp} + {inp}")
        #         return rec(inp//numExchange, total)
        # return rec(numBottles, total)

        res = 0

        while numBottles >= numExchange:
            n = numBottles // numExchange
            
            res += n*numExchange
            numBottles -= n*numExchange
            numBottles += n
            

        return numBottles + res