# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/?envType=daily-question&envId=2025-01-06


class Solution:
    # brute force n + n*m
    def minOperations(self, boxes: str) -> list[int]:
        balls = []
        N = len(boxes)
        for i in range(N):
            if boxes[i] == "1":
                balls.append(i)

        res = [0] * len(boxes)
        for i in range(N):
            for j in range(len(balls)):
                res[i] += abs(i - balls[j])

        return res
    

class Solution:
    # neeted 2n
    def minOperations(self, boxes: str) -> list[int]:
        N = len(boxes)
        res = [0] * N

        balls, moves = 0
        for i in range(N):
            res[i] = balls + moves

            moves = balls + moves
            balls += int(boxes[i])

        balls, moves = 0
        for i in reversed(range(N)):
            res[i] += balls + moves

            moves = balls + moves
            balls += int(boxes[i])

        return res

