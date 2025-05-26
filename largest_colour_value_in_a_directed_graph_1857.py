# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/?envType=daily-question&envId=2025-05-26
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:

        # could use stack instead of dfs but need to bake cake

        loop = float("inf")

        # dfs
        N = len(colors)
        cc = [[0] * 26 for _ in range(N)]
        visited = [0] * N

        adjacency = defaultdict(list)

        for u, v in edges:
            adjacency[u].append(v)

        def dfs(node):
            if visited[node] == 1:
                return loop
            if visited[node] == 2:
                return cc[node][ord(colors[node]) - ord('a')]
            
            visited[node] = 1
            for nxt in adjacency[node]:
                res = dfs(nxt)

                if res == loop:
                    return loop
                for c in range(26):
                    cc[node][c] = max(cc[node][c], cc[nxt][c])

            col = ord(colors[node]) - ord('a')
            cc[node][col] += 1
            visited[node] = 2

            return cc[node][col]
        
        ans = 0
        for i in range(N):
            val = dfs(i)
            if val == loop:
                return -1
            ans = max(ans, val)

        return ans