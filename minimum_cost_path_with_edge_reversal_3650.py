# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/description/?envType=daily-question&envId=2026-01-27
# from collections import defaultdict
import heapq

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        connections = [[] for _ in range(n)]

        for a, b, c in edges:
            connections[a].append((b, c))
            connections[b].append((a, 2*c))

        heap = [(0, 0)]
        visited = [False] * n

        max_d = 1000 * n * 2
        d = [max_d] * n
        d[0] = 0

        while heap:

            cur_d, node = heapq.heappop(heap)

            if node == n-1:
                return cur_d
            
            if visited[node]:
                continue

            visited[node] = True

            for next, cost in connections[node]:
                new_d = cur_d + cost
                if new_d < d[next]:
                    d[next] = new_d
                    heapq.heappush(heap, (new_d, next))
        
        return -1