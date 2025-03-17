# maximum_number_of_k_divisible_components_2872
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/description/?envType=daily-question&envId=2024-12-21

from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res = 0

        def dfs(cur, parent):
            total = values[cur]

            for child in adj[cur]:
                if child != parent:
                    total += dfs(child, cur)

            if total % k == 0:
                nonlocal res
                res += 1

            return total
        
        dfs(0, -1)
        
        
        return res
        