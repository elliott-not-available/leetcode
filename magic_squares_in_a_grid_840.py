# https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2025-12-30

class Solution:
    def is_magic(self, grid, r, c):
        m = grid[r][c] + grid[r][c+1] + grid[r][c+2]
        seen =set()

        for i in range(3):
            for j in range(3):
                n = grid[r+i][c+j]
                if n<1 or n>9 or n in seen:
                    return False
                seen.add(n)

        for i in range(3):
            if grid[r][c+i]+grid[r+1][c+i]+grid[r+2][c+i] != m:
                return False
            if grid[r+i][c]+grid[r+i][c+1]+grid[r+i][c+2] != m:
                return False
        
        if grid[r][c]+ grid[r+1][c+1] + grid[r+2][c+2] != m:
            return False
        if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != m:
            return False
        return True


    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rs, cs = len(grid), len(grid[0])
        res = 0

        for i in range(rs-2):
            for j in range(cs-2):
                if self.is_magic(grid, i, j):
                    res += 1
        
        
        
        
        return res