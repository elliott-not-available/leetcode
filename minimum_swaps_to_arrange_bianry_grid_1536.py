# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/?envType=daily-question&envId=2026-03-02

class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:

        n = len(grid)
        zeros = []

        for r in grid:
            cnt = 0

            for j in range(n-1, -1, -1):
                if r[j] == 0:
                    cnt += 1
                else:
                    break
            zeros.append(cnt)

        res = 0

        for i in range(n):
            needed = n - i - 1
            j = i
            while j<n and zeros[j]<needed:
                j+=1
            
            if j==n:
                return -1
            
            while j<i:
                zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                j-=1
                res += 1
        return res