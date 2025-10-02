# https://leetcode.com/problems/water-bottles-ii/?envType=daily-question&envId=2025-10-02
import math

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        ## initial solution - didnt work as i didnt realise numexchange increased after each exchange
        ## drink all (res += cur)
        ## exchange all
        ## reapeat till <numExchange


        # res = 0
        # empty = 0

        # while numBottles:
        #     print(f"cur drank: {res}")
        #     # drink all bottles
        #     res += numBottles

        #     # count extra empty bottles
        #     empty += numBottles

        #     # how many exchanges can we do
        #     n_exchanges =  empty // numExchange

        #     print(f"cur bottles: {numBottles}")
        #     print(f"added to empty: {empty}")
        #     print(f"exchanging : {n_exchanges}")

        #     # do exchange from empty to full
        #     empty -= n_exchanges*numExchange
        #     print(f"leftover empty : {empty}")
        #     numBottles = n_exchanges
        # return res
        #

        ###################################################

        ## sim sol
        # res = numBottles
        # empty = numBottles

        # while empty >= numExchange:
        #     res += 1
        #     empty -= (numExchange + 1)
        #     numExchange += 1
        # return res


        ## editorial equation solution: series formula?
        a = 1
        b = 2 * numExchange - 3
        c = -2 * numBottles
        delta = b * b - 4 * a * c
        t = math.ceil((-b + math.sqrt(delta)) / (2 * a))
        return numBottles + t - 1