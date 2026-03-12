# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/?envType=daily-question&envId=2026-03-12

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        # correct answer seems to be dsu + heapq. cba
        
        res = 10**5
        m = 0
        for e in edges:
            if e[-1]==1:
                res = min(res, e[2])
            else:
                m = max(m, e[2])

        return m if res==10**5 else res