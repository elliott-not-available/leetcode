# https://leetcode.com/problems/find-eventual-safe-states/?envType=daily-question&envId=2025-01-24

class Solution:
    # dfs recursive
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:

        N = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
            safe[i] = True
            return safe[i]

        res = []
        for i in range(N):
            if dfs(i):
                res.append(i)

        return res
        