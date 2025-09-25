# https://leetcode.com/problems/triangle/description/?envType=daily-question&envId=2025-09-25
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # res = triangle[0][0]
        # cur = 0

        # for row in triangle[1:]:
            

        #     if row[cur] < row[cur+1]:
        #         res += row[cur]
        #     else:
        #         res += row[cur+1]
        #         cur += 1


        # return res
        res = triangle

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[i][j] += min(res[i+1][j], res[i+1][j+1])
        return res[0][0]