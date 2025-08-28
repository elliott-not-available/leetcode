# https://leetcode.com/problems/sort-matrix-by-diagonals/description/?envType=daily-question&envId=2025-08-28

from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)

        for i in range(n):

            store = [grid[i+j][j] for j in range(n-i)]
            store.sort(reverse=True)
            # print(store)

            for k in range(len(store)):
                grid[i+k][k] = store[k]

        for j in range(1,n):
            store = [grid[i][j+i] for i in range(n-j)]
            store.sort()

            for k in range(len(store)):
                grid[k][k+j] = store[k]

        return grid
        
        
        return 