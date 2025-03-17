# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/?envType=daily-question&envId=2025-03-14
# from heapq import heapify, heappush, heappop
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:

        # # bruteish force
        # N = len(candies)
        csum = sum(candies)

        if csum < k:
            return 0
        
        # min_v = min(candies)

        # if N >= k:
        #     return min_v
        

        # heapvals = [-1*v for v in candies]
        # heapify(heapvals)

        # # do some algorithm 
        # new_len = N 
        # while k > new_len:
        #     # think i need to use an ordered stack and pop max
        #     # split max in 2

        #     cur = heappop(heapvals)
        #     if cur == -1:
        #         return 0
        #     new_val = cur // 2
        #     if cur % 2 == 1:
        #         heappush(heapvals, new_val - 1)
        #         heappush(heapvals, new_val)
        #     else:
        #         heappush(heapvals, new_val)
        #         heappush(heapvals, new_val)
        #     new_len += 1

        #     min_v = min(min_v, new_val * -1)

        # # ret
        # return min_v


        # use binary search
        l = 1
        r = csum // k
        res = 0

        while l <= r:
            m = (l + r) // 2
            cnter = 0
            for c in candies:
                if c >= m:
                    cnter += c // m
                if cnter >= k:
                    break

            if cnter >= k:
                res = m
                l = m + 1
            else:
                r = m - 1
                
        return res




        