# https://leetcode.com/problems/apply-operations-to-maximize-score/?envType=daily-question&envId=2025-03-29
from math import sqrt
from heapq import heapify, heappop, heappush
class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:

        res = 1
        N = len(nums)
        MOD = 10**9 + 7

        prime_scores = []

        for n in nums:
            score = 0
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    score += 1
                    while n % f == 0:
                        n = n // f

            if n >= 2:
                score += 1
            prime_scores.append(score)

        left_bound = [-1] * N
        right_bound = [N] * N

        stack = []

        for i, s in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < s:
                ind = stack.pop()
                right_bound[ind] = i

            if stack:
                left_bound[i] = stack[-1]

            stack.append(i)

        min_heap = [(-n, i) for i, n in enumerate(nums)]
        
        heapify(min_heap)

        while k > 0:
            n, index = heappop(min_heap)
            n = -n
            score = prime_scores[index]

            lc = index - left_bound[index]
            rc = right_bound[index] - index

            cnt = lc * rc
            operations = min(cnt, k)

            res = (res * pow(n, operations, MOD)) % MOD

            k -= operations


        return res
