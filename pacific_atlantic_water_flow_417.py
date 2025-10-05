# https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=daily-question&envId=2025-10-05

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        r, c = len(heights), len(heights[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(i, j, visited):

            visited.add((i,j))

            for dx, dy in dirs:
                x,y = i + dx, j + dy

                #boundry
                if 0 <= x < r and 0 <= y < c:
                    
                    #visited and flow up
                    if (x,y) not in visited and heights[x][y] >= heights[i][j]:
                        dfs(x,y, visited)

        pac, atl = set(), set()

        for i in range(c): dfs(0, i, pac)
        for j in range(r): dfs(j, 0, pac)

        for i in range(c): dfs(r-1, i, atl)
        for j in range(r): dfs(j, c-1, atl)

        
        return list( pac & atl )