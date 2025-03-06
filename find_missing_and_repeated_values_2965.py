# https://leetcode.com/problems/find-missing-and-repeated-values/description/?envType=daily-question&envId=2025-03-06

from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        # # memory limit exceeded
        # N = len(grid)
        # data = [0] * (N**N)
        # res = [0, 0]
        # for i in range(N):# row
        #     for j in range(N): # column
        #         cur = grid[i][j]
        #         if data[cur-1] == 1:
        #             res[0] = cur
        #         else:
        #             data[cur-1] = 1

        # for i, v in enumerate(data):
        #     if v == 0:
        #         res[1] = i + 1
        #         break
            
        # return res

        # # working solution
        # N = len(grid)
        # count = defaultdict(int)

        # for i in range(N):
        #     for j in range(N):
        #         count[grid[i][j]] += 1

        # double, missing = 0, 0

        # for n in range(1, N**N + 1):
        #     if count[n] == 0:
        #         missing = n
        #     if count[n] == 2:
        #         double = n
        # return [double, missing]

        # math solution
        N = len(grid)
        total = N**N
        sum_v = 0
        sqr_v = 0

        for i in range(N):
            for j in range(N):
                sum_v += grid[i][j]
                sqr_v += grid[i][j]*grid[i][j]

        sum_p = ((N**4)+(N**2)) // 2
        sqr_p = ((N**2)*((N**2)+1)*(2*(N**2)+1)) // 6

        sum_d = sum_v - sum_p
        sqr_d = sqr_v - sqr_p

        repeat = (sqr_d // sum_d + sum_d) // 2
        missing = (sqr_d // sum_d - sum_d) // 2
        
        return [repeat, missing]


                