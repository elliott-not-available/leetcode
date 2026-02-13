# https://leetcode.com/problems/longest-balanced-substring-ii/description/?envType=daily-question&envId=2026-02-13
from collections import defaultdict#, Counter


class Solution:
    def longestBalanced(self, s: str) -> int:

        
        # too slow
        # def check_counter(cntr):
        #     return len(set(cntr.values()))==1
        
        # # c = Counter(s)
        # # if check_counter(c):
        # #     return len(s)

        # max_l = 0
        # n = len(s)

        # for i in range(n):
        #     c = defaultdict(int)
        #     for j in range(i, n):
        #         c[s[j]] += 1
        #         if check_counter(c):
        #             max_l = max(max_l, j-i + 1)

        # return max_l


        n = len(s)
        pre = [[0,0,0]]

        for c in s:
            pre.append(pre[-1])
            pre[-1]["abc".index(c)] += 1

        res = 0
        m = {}
        for i, (a, b, c) in enumerate(pre):
            for k in [
                (-1, a - b, a - c), # a,b,c
                (-2, a - b, c),     # a,b
                (-3, b - c, a),     # b,c
                (-4, c - a, b),     # a,c
                (-5, b, c),         # a
                (-6, c, a),         # b
                (-7, a, b),         # c
            ]:
                if not k in m: m[k] = i
                else: res = max(res, i - m[k])
        return res