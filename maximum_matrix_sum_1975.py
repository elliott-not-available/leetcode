# maximum_matrix_sum_1975
# https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2024-11-24

class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        cnt_neg = 0
        cnt = 0
        min_val = 1000000
        for row in matrix:
            for c in row:

                abs_c = abs(c)
                if abs_c < min_val:
                    min_val = abs_c

                cnt += abs_c
                if c <= 0:
                    cnt_neg += 1

        print(cnt)
        print(min_val)

        if min_val == 0:
            return cnt
        
        if cnt_neg & 1:
            return cnt - 2*min_val
        
        return cnt
        