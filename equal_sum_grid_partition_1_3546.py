# https://leetcode.com/problems/equal-sum-grid-partition-i/description/?envType=daily-question&envId=2026-03-25

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        
        if total % 2:
            return False
        
        target = total // 2
        s = 0
        
        for i in range(m - 1):
            s += sum(grid[i])
            if s == target:
                return True
        
        s = 0
        
        for j in range(n - 1):
            for i in range(m):
                s += grid[i][j]
            if s == target:
                return True
        
        return False