# count_square_submatrices_with_all_ones_1277
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2024-10-27

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:

        # brute force would be scan matrix i,j: 
        # for each i,j check how many sub-1-matrices you can make

        # recursive maximal-submatrices problem

        rows = len(matrix)
        cols = len(matrix[0])
        cache = {}

        def dfs(i, j):
            if i == rows or j == cols or not matrix[i][j]:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            cache[(i, j)] = 1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
            return cache[(i, j)]
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res += dfs(r, c)
       
        return res