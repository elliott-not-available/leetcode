# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/description/?envType=daily-question&envId=2025-05-14

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 7

        transform = [[0]*26 for _ in range(26)]
        for i in range(26):
            for shift in range(nums[i]):
                transform[i][(i+1+shift) % 26] += 1

        def multiply_matrices(a, b):
            rows_a, cols_a, cols_b = len(a), len(a[0]), len(b)
            r = [[0]*cols_b for _ in range(rows_a)]
            for i in range(rows_a):
                for j in range(cols_b):
                    tmp = 0
                    for k in range(cols_a):
                        tmp += a[i][k] * b[k][j]
                    r[i][j] = tmp % MOD
            return r

        def power_matrix(matrix, expo):
            n = len(matrix)
            r = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
            while expo > 0:
                if expo & 1:
                    r = multiply_matrices(r, matrix)
                matrix = multiply_matrices(matrix, matrix)
                expo >>= 1
            return r
        
        transform = power_matrix(transform, t)
        freq = [[0]*26]

        for ch in s:
            freq[0][ord(ch) - ord('a')] += 1
        freq = multiply_matrices(freq, transform)
        return sum(freq[0]) % MOD