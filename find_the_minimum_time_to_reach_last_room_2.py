from heapq import heapify, heappop, heappush

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        # min heap / djikstra
        # same as yesterday but keep track of n_moves and use for calculating score
        N = len(moveTime)
        M = len(moveTime[0])
        visited = [[0]*M for _ in range(N)]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        m_heap = []

        heappush(m_heap, (0, 0, 0, 0)) #(score, move_n, i, j))

        while m_heap:

            score, move_n, i, j = heappop(m_heap)

            if i == N-1 and j == M-1:
                return score

            if visited[i][j]:
                continue
            visited[i][j] = 1

            move_n += 1
            for di, dj in moves:
            
                n_i, n_j = i+di, j+dj

                if not (0 <= n_i <= N-1 and 0 <= n_j <= M-1):
                    continue

                # add move to heap, check move_n+1 is even 
                # first move +1, second move +2
                ad = 1 if (move_n) % 2 else 2
                n_score = max(score+ad, moveTime[n_i][n_j]+ad)
                print(n_i, n_j, n_score, move_n)

                heappush(m_heap, (n_score, move_n, n_i, n_j))

        return -1
        