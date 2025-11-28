# https://leetcode.com/problems/maximum-number-of-k-divisible-components/?envType=daily-question&envId=2025-11-28

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        # dfs

        adj = [[] for _ in range(n)]

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        component_count = [0]
        
        self.dfs(0, -1, adj, values, k, component_count)
        return component_count[0]

    def dfs(self, current_node, parent_node, adj, node_values, k, component_count):
        suma = 0

        for nn in adj[current_node]:
            if nn != parent_node:
                suma += self.dfs(nn, current_node, adj, node_values, k, component_count)
                suma %= k
        suma += node_values[current_node]
        suma %= k

        if suma == 0:
            component_count[0] += 1
        return suma