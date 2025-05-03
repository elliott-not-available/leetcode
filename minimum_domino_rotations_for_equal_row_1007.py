# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/?envType=daily-question&envId=2025-05-03

from collections import Counter

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        
        # a = Counter(tops)
        # b = Counter(bottoms)

        # a_m = max(a, key=a.get)
        # b_m = max(b, key=b.get)
        
        # if a[a_m] >= b[b_m]:
        #     static = tops
        #     swap = bottoms
        #     m = a_m
        # else:
        #     static = bottoms
        #     swap = tops
        #     m = b_m

        # res = 0

        # for i in range(len(tops)):
        #     if static[i] == m:
        #         continue
        #     elif swap[i] == m:
        #         res += 1
        #     else: 
        #         return -1

        # return res
        ############################################
        # brute force - not checking bottoms

        # N = len(tops)
        # min_swaps = 20000

        # for i in range(1,7):
        #     swaps = 0

        #     for j in range(N):

        #         if tops[j] == i:
        #             continue
        #         elif bottoms[j] == i:
        #             swaps += 1
        #         else:
        #             swaps = -1
        #             break

        #     if swaps > 0:
        #         min_swaps = min(min_swaps, swaps, abs(N - min_swaps))
        # return -1 if min_swaps == 20000 else min_swaps
        ################################################
        # brute force - checking both bot + top for top[0] bot[0]

        def swaps(target):
            swap_t, swap_b = 0, 0

            for i in range(len(tops)):

                if tops[i] != target and bottoms[i] != target:
                    return float('inf')
                if tops[i] != target:
                    swap_t += 1
                if bottoms[i] != target:
                    swap_b += 1

            return min(swap_b, swap_t)
        
        res = min(swaps(tops[0]), swaps(bottoms[0]))
        return -1 if res == float('inf') else res
