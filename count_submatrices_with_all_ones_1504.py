# https://leetcode.com/problems/count-submatrices-with-all-ones/description/?envType=daily-questackion&envId=2025-08-21

class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        # i would say hard not medium (had to use top solution)

        rows, cols = len(mat), len(mat[0])

        heights = [0] * cols
        res = 0

        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if mat[i][j] else 0
            
            count = [0] * cols
            stack = []

            for j in range(cols):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                if stack:
                    p = stack[-1]
                    count[j] = count[p] + heights[j] * (j-p)
                else:
                    count[j] = heights[j] * (j+1)
                stack.append(j)
                res += count[j]
        return res
        