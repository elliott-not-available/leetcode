# https://leetcode.com/problems/most-profitable-path-in-a-tree/description/?envType=daily-question&envId=2025-02-24

from collections import defaultdict, deque


class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # bob sim dfs
        bob_times = {}
        def dfs(src, pre, time):
            if src == 0:
                bob_times[src] = time
                return True
            for nei in adj[src]:
                if nei == pre:
                    continue
                
                if dfs(nei, src, time + 1):
                    bob_times[src] = time
                    return True
            return False

        dfs(bob, -1, 0)

        # alice sim bfs

        q = deque([(0, 0, -1, amount[0])]) # node, time, parent, total profit
        res = float("-inf")
        while q:
            node, time, parent, profit = q.popleft()

            for nei in adj[node]:
                if nei == parent:
                    continue
                nei_profit = amount[nei]
                nei_time = time + 1

                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        nei_profit = 0
                    if nei_time == bob_times[nei]:
                        nei_profit = nei_profit // 2

                tot_profit = profit + nei_profit
                q.append((nei, nei_time, node, tot_profit))
                if len(adj[nei]) == 1:
                    res = max(res, tot_profit)

        return res
        