# https://leetcode.com/problems/largest-triangle-area/description/?envType=daily-question&envId=2025-09-27
from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        # bruteforce all triangles
        largest = 0
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    largest = max(largest, area(points[i], points[j], points[k]))



        return largest