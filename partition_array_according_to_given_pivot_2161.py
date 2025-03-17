# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2025-03-03

from collections import defaultdict

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        # less = defaultdict(int)
        # more = defaultdict(int)
        less = []
        more = []
        same = []

        for n in nums:
            if n < pivot:
                less.append(n)
                # less[n] += 1
            if n > pivot:
                more.append(n)
                # more[n] += 1
            if n == pivot:
                same.append(n)

        # res = []
        # for n in sorted(less.keys()):
            # if less[n] > 0:
            #     res += [n] * less[n]
        res = less + same + more
        # res += same

        # for m in sorted(more.keys()):
            # if more[m] > 0:
            #     res += [m] * more[m]

        return res
        