# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/solutions/6754794/dp-in-depth-with-images-example-walkthrough-c-python-java/?envType=daily-question&envId=2025-05-18

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        # total number of row combinations
        total = 3**m

        pattern = [[] for _ in range(total)]
        good = []

        # for each row comb, create pattern, list good ones
        for i in range(total):
            value = i
            valid = True
            # unsure how this creates ALL patterns?
            for _ in range(m):
                pattern[i].append(value % 3)
                value //= 3

            # if
            for j in range(1,m):
                if pattern[i][j] == pattern[i][j-1]:
                    valid=False
                    # break?
                    break
            
            if valid:
                good.append(i)

        dp = [[0]*total for _ in range(n+1)]

        # set row 1 index with 1 for each good pattern
        for i in good:
            dp[1][i] = 1

        row_valid = [[0]*total for _ in range(total)]
        #
        for i in good:
            for j in good:
                row_valid[i][j] = 1
                for k in range(m):
                    if pattern[i][k] == pattern[j][k]:
                        row_valid[i][j] = 0

        for col in range(2, n+1):
            for i in good:
                tot = 0
                for j in good:
                    if row_valid[i][j]:
                        tot += dp[col-1][j]

                dp[col][i] = tot % MOD
        return sum(dp[n]) % MOD
