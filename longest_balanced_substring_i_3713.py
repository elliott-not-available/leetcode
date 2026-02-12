# https://leetcode.com/problems/longest-balanced-substring-i/description/?envType=daily-question&envId=2026-02-12
from collections import defaultdict#, Counter
class Solution:
    def longestBalanced(self, s: str) -> int:
        
        # c = Counter(s)

        def check_counter(cntr: defaultdict) -> bool:

            # vals = list(cntr.values())
            # default = vals[0]

            # for v in vals:
            #     if v != default:
            #         return False
            # return True
            return len(set(cntr.values()))==1


        # i think there is a 2 pass 2 pntr solution that is more optimised
        max_l = 0
        n = len(s)

        for i in range(n):
            cntr = defaultdict(int)
            for j in range(i, n):
                cntr[s[j]] += 1
                if check_counter(cntr):
                    max_l = max(max_l, len(cntr.values()))



        return max_l