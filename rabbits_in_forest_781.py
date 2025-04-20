# https://leetcode.com/problems/rabbits-in-forest/?envType=daily-question&envId=2025-04-20

from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        c = Counter(answers)
        res = 0
        for v in c:
            v_count = c[v]
            # number that said same value / total of value
            # this will get the min number of groups of size v+1
            n = ceil((v_count) / (v + 1))

            res += n*(v+1)




        return res