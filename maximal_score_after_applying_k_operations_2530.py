# maximal_score_after_applying_k_operations_2530
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/?envType=daily-question&envId=2024-10-14
import heapq
import math


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        pq = [-n for n in nums]
        heapq.heapify(pq)
        score = 0

        for i in range(k):
            # find the max
            # store score
            # replace max

            c_max = -heapq.heappop(pq)
            score += c_max

            heapq.heappush(pq, -math.ceil(c_max / 3))
        return score


