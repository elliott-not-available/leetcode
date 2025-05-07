# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/?envType=daily-question&envId=2025-05-07
from heapq import heapify, heappop, heappush
class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:

        # min heap
        N = len(moveTime)
        M = len(moveTime[0])
        visited = [[0]*M for _ in range(N)]
        heap = []
        i, j = 0, 0
        cur_score = 0
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        

        heappush(heap, (cur_score, i, j))
        
        while heap:

            cur, i, j = heappop(heap)

            if i == N-1 and j == M-1:
                return cur

            if visited[i][j]:
                continue
            visited[i][j] = 1

            for m in moves:
                n_i, n_j = i + m[0], j + m[1]

                if not (0 <= n_i <= N-1 and 0 <= n_j <= M-1):
                    continue

                n_s = max(cur + 1, moveTime[n_i][n_j] + 1)
                
                heappush(heap, (n_s, n_i, n_j))

        # return