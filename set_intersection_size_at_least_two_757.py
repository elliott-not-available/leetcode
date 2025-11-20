# https://leetcode.com/problems/set-intersection-size-at-least-two/description/?envType=daily-question&envId=2025-11-20

class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        print(intervals)

        res = 0
        pre = []

        for s, e in intervals:
            if not pre or pre[1]<s:
                res += 2
                pre = [e-1, e]
            elif pre[0] <s:
                pre = [pre[1], e]
                res += 1
        return res