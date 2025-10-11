# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/?envType=daily-question&envId=2025-10-11
from collections import Counter
class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        c = Counter(power)
        sorted_c = [(-(10**9), 0)]
        for k in sorted(c.keys()):
            sorted_c.append((k, c[k]))

        n = len(sorted_c)
        res = [0] * n
        max_p = 0
        j = 1

        for i in range(1, n):
            while j<i and sorted_c[j][0] < sorted_c[i][0] - 2:
                max_p = max(max_p, res[j])
                j += 1
            res[i] = max_p + sorted_c[i][0] * sorted_c[i][1]
        return max(res)