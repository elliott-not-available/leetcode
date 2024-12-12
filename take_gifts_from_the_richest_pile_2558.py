# https://leetcode.com/problems/take-gifts-from-the-richest-pile/?envType=daily-question&envId=2024-12-12
import math

class Solution_og:
    # quite slow
    def pickGifts(self, gifts: list[int], k: int) -> int:

        def asd():
            max_v = 0
            for i in range(len(gifts)):
                if gifts[i] > max_v:
                    max_v = gifts[i]
                    max_i = i

            return max_i
        
        for _ in range(k):
            max_i = asd()
            gifts[max_i] = math.floor(math.sqrt(gifts[max_i]))

        return sum(gifts)

import heapq

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts_heap = [-gift for gift in gifts]
        heapq.heapify(gifts_heap)

        for _ in range(k):
            max_ele = -heapq.heappop(gifts_heap)
            heapq.heappush(gifts_heap, -math.floor(math.sqrt(max_ele)))        

        return -sum(gifts_heap)
