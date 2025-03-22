# https://leetcode.com/problems/count-the-number-of-complete-components/description/?envType=daily-question&envId=2025-03-22

from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:

        # going to need adjacentcy set and visited set
        # for each value (if not in visited) run dfs to group all in same comp
        # dfs adds to visited and recursively checks adjacency list

        # to make sure comp is complete, check each node has len(comp) - 1 edges
        
        def dfs(v, res):
            if v in visit:
                return
            
            visit.add(v)
            res.append(v)

            for nei in adj[v]:
                dfs(nei, res)
            return res
        
        adj = defaultdict(list)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        res = 0
        visit = set()

        for v in range(n):

            if v in visit:
               continue 

            component = dfs(v, [])
            if all([len(component) - 1 == len(adj[v2]) for v2 in component]):
                res += 1
            # flag = True
            # for v2 in component:
            #     if len(component) - 1 != len(adj[v2]):
            #         flag = False
            #         break
            # if flag:
            #     res += 1


        return res