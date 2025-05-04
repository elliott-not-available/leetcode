# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        # can probs do some fancy count() + combinatorics stuff.
        visited = defaultdict(int)
        res = 0

        for d in dominoes:

            s = sorted(d)

            if (s[0], s[1]) in visited:
                res += visited[(s[0], s[1])]
            visited[(s[0], s[1])] += 1


        return res