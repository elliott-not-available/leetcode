# shortest_distance_after_road_addition_queries_1_3243
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/?envType=daily-question&envId=2024-11-27
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:

        neighbours = [[i+1] for i in range(n)]

        def shortest_path():
            q = deque()
            q.append((0,0))
            visited = set()
            visited.add((0, 0))

            while q:
                cur, length = q.popleft()

                if cur == n-1:
                    return length
                
                for nei in neighbours[cur]:
                    if nei not in visited:
                        q.append((nei, length + 1))
                        visited.add(nei)

        res = []

        for src, dst in queries:
            neighbours[src].append(dst)
            shortest_path()
            res.append(shortest_path())


        return res
        