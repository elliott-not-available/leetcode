# https://leetcode.com/problems/pyramid-transition-matrix/description/?envType=daily-question&envId=2025-12-29
from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:

        data = defaultdict(set)

        for u, v, w in allowed:
            data[(u, v)].add(w)

        def neb(node):

            res = [""]

            for i in range(1, len(node)):
                mat = data[(node[i-1], node[i])]

                if mat:
                    res = [a+b for b in mat for a in res]
                else:
                    return []
            return res
        
        visited = set()

        def dfs(node):
            if len(node)==1:
                return True
            if node in visited:
                return False
            
            for n in neb(node):
                if dfs(n):
                    return True
            
            visited.add(node)
            return False
        return dfs(bottom)