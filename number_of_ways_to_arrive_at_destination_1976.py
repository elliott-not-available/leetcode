# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/?envType=daily-question&envId=2025-03-23

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:

        # build adjacency (and time?) list
        # visited set
        # dfs? if visited or greater than minval early exit

        # not working currently, i have made a mistake somewhere. I think minstack might be most efficient.

        adj = defaultdict(list)

        for r in roads:
            adj[r[0]].append((r[1], r[2]))
            adj[r[1]].append((r[0], r[2]))

        # minval = float("inf")

        # def dfs(node, time, minval, visited, res):

        #     if node in visited:
        #         return
            
        #     if time > minval:
        #         return
            
        #     if node == n:
        #         if time < minval:
        #             minval = time
        #             res = 1
        #         elif time == minval:
        #             res += 1

        #     visited.append(node)

        #     for nei, cost in adj[node]:
        #         dfs(nei, time+cost, minval, visited, res)

        #     return res

        # return dfs(0,0, minval, [], 0)

        MOD = 10**9 + 7
        min_heap = [(0,0)] #(cost, node)
        min_cost = [float("inf")] * n
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            cost, node = heappop(min_heap)

            for nei, nei_cost in adj[node]:

                cur_cost = cost + nei_cost

                if cur_cost < min_cost[nei]:
                    min_cost[nei] = cur_cost
                    path_count[nei] = path_count[node]
                    heappush(min_heap, (cur_cost, nei))
                elif cur_cost == min_cost[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD

        return path_count[n-1]
            

        