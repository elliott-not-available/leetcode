# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/?envType=daily-question&envId=2025-10-08
import math
import bisect

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        # # brute force
        # res = []
        # potions.sort()

        # for s in spells:
        #     cur = 0
        #     for i in range(len(potions)):

        #         product = s * potions[i]

        #         if product >= success:
        #             cur = len(potions) - i
        #             break

        #     res.append(cur)

        # return res

        ## uses bisect instead of second loop, and early exit
        potions.sort()
        res = []

        for s in spells:
            min_potion_val = math.ceil(success / s)
            if min_potion_val > potions[-1]:
                res.append(0)
                continue

            ind = bisect.bisect_left(potions, min_potion_val)
            res.append(len(potions) - ind)
        return res
        