# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=daily-question&envId=2025-05-21

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        zero_row = []
        zero_col = []

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_col.append(j)


        for z in zero_row:
            matrix[z] = [0] * n

        for z in zero_col:

            for i in range(m):
                matrix[i][z] = 0

        