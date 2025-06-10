# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10

from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        # find max odd
        # find min even
        
        c = Counter(s)
        # print(c)


        max_odd = 0
        min_even = 100

        for _, v in c.items():

            # max odd
            if v % 2:
                max_odd = max(max_odd, v)
                # if v > max_odd:
                #     max_odd = v

            # min even
            else:
                min_even = min(min_even, v)
                # if v < min_even:
                #     min_even = v

        return max_odd - min_even
        