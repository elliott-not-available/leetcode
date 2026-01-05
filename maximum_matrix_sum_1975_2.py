# https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2026-01-05

class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:

        cnt_neg = 0
        cnt = 0
        min_val = 100000

        for r in matrix:
            for v in r:

                abs_v = abs(v)
                cnt += abs_v

                if abs_v < min_val:
                    min_val = abs_v
                
                if v < 0:
                    cnt_neg += 1

        if cnt_neg & 1:
            return cnt - 2*min_val

        return cnt