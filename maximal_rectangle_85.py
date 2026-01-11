# https://leetcode.com/problems/maximal-rectangle/description/?envType=daily-question&envId=2026-01-11
# from looking at solutions it seems collecting "histogram" data + using stack to compare is more efficient
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        int_matrix = matrix

        for i in range(n):
            for j in range(m):
                int_matrix[i][j] = int(int_matrix[i][j])

        # row prefix - create cur max width for each value in each row
        for i in range(n):
            for j in range(1, m):
                # # print("i am workin")
                # if matrix[i][j] == "0":
                #     matrix[i][j] == 0

                if int_matrix[i][j] == 1:
                    int_matrix[i][j] = int_matrix[i][j-1] + 1

        res = 0
        # print(int_matrix)

        # col
        for j in range(m):
            # row
            for i in range(n):

                cur_width = int_matrix[i][j]

                if cur_width == 0:
                    continue

                # search column to find max rect
                k = i
                cw = cur_width
                while k < n and int_matrix[k][j] > 0:
                    cw = min(cw, int_matrix[k][j])
                    h = k - i + 1
                    res = max(res, cw*h)
                    k += 1

                k = i
                cw = cur_width
                while k >= 0 and int_matrix[k][j] > 0:
                    cw = min(cw, int_matrix[k][j])
                    h = i - k + 1
                    res = max(res, cw*h)
                    k-=1


        return res