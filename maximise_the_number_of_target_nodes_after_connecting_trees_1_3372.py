# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/?envType=daily-question&envId=2025-05-28

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:

        def build_adj(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]

            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        def dfs(adj, u, p, k):
            if k <0:
                return 0

            cnt = 1
            for v in adj[u]:
                if v != p:
                    cnt += dfs(adj, v, u, k - 1)
            return cnt
        
        adj1 = build_adj(edges1)
        adj2 = build_adj(edges2)

        maxi = 0

        for i in range(len(adj2)):
            maxi = max(maxi, dfs(adj2, i, -1, k-1))

        res = []

        for j in range(len(adj1)):
            res.append(dfs(adj1, j, -1, k) + maxi)

        return res