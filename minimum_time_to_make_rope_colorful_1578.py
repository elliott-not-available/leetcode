# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/?envType=daily-question&envId=2025-11-03

class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res = 0
        for i in range(1, len(colors)):

            if colors[i] == colors[i-1]:
                res += min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
                    

        return res
        