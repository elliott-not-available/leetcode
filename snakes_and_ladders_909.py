# https://leetcode.com/problems/snakes-and-ladders/description/?envType=daily-question&envId=2025-05-31

from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:

        N = len(board)
        min_rolls = [-1] * (N * N + 1)
        qq = deque()
        min_rolls[1] =  0
        qq.append(1)

        while qq:
            cur = qq.popleft()

            for i in range(1, 7):

                
                n = cur + i
                if n > N*N:
                    break

                row = (n - 1) // N
                col = (n - 1) % N

                v = board[N-1-row][(N-1-col) if (row%2==1) else col]
                y = v if v>0 else n

                if y == N*N:
                    return min_rolls[cur] + 1
                
                if min_rolls[y] == -1:
                    min_rolls[y] = min_rolls[cur] + 1
                    qq.append(y)



        return -1
        