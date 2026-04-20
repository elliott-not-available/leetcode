# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        # can probs sneak in some early exit
        n=len(colors)
        res = 0
        for i in range(n):
            for j in range(n-1,i,-1):
                # print(i,j)
                if colors[i]!=colors[j]:
                    res=max(res, j-i)

        return res