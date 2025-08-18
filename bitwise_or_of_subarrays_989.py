# https://leetcode.com/problems/bitwise-ors-of-subarrays/description/?envType=daily-question&envId=2025-07-31
from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # brute force too slow
        # uniq = set()
        # res = 0
        # n = len(arr)

        # if n == 1:
        #     return 1

        # for i in range(n-1):
        #     for j in range(i, n):

        #         if i == j:
        #             cur = arr[i]
        #         else:
        #             cur = cur | arr[j]

        #         if cur not in uniq:
        #             res += 1
        #             uniq.add(cur)

        # return res

        uniq = set()
        cur = set()

        for a in arr:
            nxt = {a | b for b in cur}
            nxt.add(a)

            uniq.update(nxt)

            cur = nxt

        return len(uniq)