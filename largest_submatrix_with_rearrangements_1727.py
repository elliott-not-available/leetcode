# https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/?envType=daily-question&envId=2026-03-17

class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev_r = [0] * n
        res = 0

        for r in range(m):
            cur_r = matrix[r][:]
            for c in range(n):
                if cur_r[c] != 0:
                    cur_r[c] += prev_r[c]

            sorted_r = sorted(cur_r, reverse=True)

            for i in range(n):
                res = max(res, sorted_r[i] * (i+1))

            prev_r = cur_r
        return res