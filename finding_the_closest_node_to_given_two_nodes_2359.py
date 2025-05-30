# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/?envType=daily-question&envId=2025-05-30

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        res, mom, N = -1, float("inf"), len(edges)

        d1 = [-1] * N
        d2 = [-1] * N

        def dfs(cur, dist, dists, edges):
            while cur != -1 and dists[cur] == -1:
                dists[cur] = dist
                dist += 1
                cur = edges[cur]

        dfs(node1, 0, d1, edges)
        dfs(node2, 0, d2, edges)

        for i in range(N):
            if d1[i] >= 0 and d2[i] >= 0:
                maxi = max(d1[i], d2[i])
                if maxi < mom:
                    mom = maxi
                    res = i
        return res