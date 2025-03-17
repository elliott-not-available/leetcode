# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/?envType=daily-question&envId=2025-02-07

from collections import defaultdict, Counter

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        # i think this is wildly inefficent, what does limit even do, im so tired
        what_are_you_used_for = limit

        res = []
        cols = Counter()
        hm = {} # defaultdict(int)
        for ind, col in queries:

            if ind in hm.keys():
                old_col = hm[ind]
                cols[old_col] -= 1

                if cols[old_col] == 0:
                    del cols[old_col]

                hm[ind] = col
                cols[col] += 1

                res.append(len(cols.keys()))
            else:
                hm[ind] = col
                cols[col] += 1

                res.append(len(cols.keys()))
            
        return res
        