# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/?envType=daily-question&envId=2025-03-25

class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:

        # draw line after each rectangle, check if it matches conditions?
        # non overlaping intervals?

        x_intervals = []
        y_intervals = []

        for x1,y1,x2,y2 in rectangles:
            x_intervals.append((x1,x2))
            y_intervals.append((y1,y2))

        x_intervals.sort()
        y_intervals.sort()

        def count_non_overlaping_intervals(intervals):
            prev = -1
            res = 0
            for a, b in intervals:
                if a >= prev:
                    res += 1
                prev = max(prev, b)
            return res
        
        x_cnt = count_non_overlaping_intervals(x_intervals)
        y_cnt = count_non_overlaping_intervals(y_intervals)

        return max(x_cnt, y_cnt) >= 3