# https://leetcode.com/problems/power-grid-maintenance/?envType=daily-question&envId=2025-11-06
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:

        ## timelimit exceeded
        # online = [True] * (c+1)
        # res = []
        # cons = defaultdict(SortedList)

        # for a,b in connections:
        #     cons[a].add(b)
        #     cons[b].add(a)

        # def dfs(i, seen):
        #     seen.add(i)
        #     for nei in cons[i]:
        #         if nei not in seen:
        #             dfs(nei, seen)


        # for query_type, i in queries:
            

        #     if query_type == 1:
        #         if online[i]:
        #             res.append(i)
        #         else:
        #             seen = set()
        #             dfs(i, seen)
        #             online_connected_nodes = [n for n in seen if online[n]]
        #             res.append(min(online_connected_nodes) if online_connected_nodes else -1)
        #     else:
        #         online[i] = False
                
        # return res

        parent = list(range(c+1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        next_node = [0] * (c+1)
        comp_min = [0] * (c+1)
        last = {}

        for i in range(1, c+1):
            r = find(i)
            if comp_min[r] == 0:
                comp_min[r] = i
            else:
                next_node[last[r]] = i
            last[r] = i

        offline = [False] * (c+1)
        res = []

        for t, x in queries:
            if t==1:
                if not offline[x]:
                    res.append(x)
                else:
                    r = find(x)
                    res.append(comp_min[r] if comp_min[r] else -1)
            else:
                if not offline[x]:
                    offline[x] = True
                    r = find(x)
                    if comp_min[r] == x:
                        y = next_node[x]
                        while y and offline[y]:
                            y = next_node[y]
                        comp_min[r] = y if y else 0

        return res