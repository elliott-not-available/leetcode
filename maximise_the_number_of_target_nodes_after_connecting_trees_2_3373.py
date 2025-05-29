# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description/?envType=daily-question&envId=2025-05-29

# from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:

        def dfs(node, parent, depth, children, colour):
            res = 1 - depth % 2
            colour[node] = depth % 2

            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, depth + 1, children, colour)
            return res
        
        def build_adj(edges, colour):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]

            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            res = dfs(0, -1, 0, adj, colour)
            return [res, n - res]
        
        n = len(edges1) + 1
        m = len(edges2) + 1
        col1 = [0] * n
        col2 = [0] * m
        cnt1 = build_adj(edges1, col1)
        cnt2 = build_adj(edges2, col2)

        res = [0] * n
        for i in range(n):
            res[i] = cnt1[col1[i]] + max(cnt2[0], cnt2[1])

        return res