# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/?envType=daily-question&envId=2025-02-27

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        # brute force: works
        # build it up maybe? pick two starting points try and get max length

        # how to optimise?
        arr_set = set(arr)

        def max_fibo(i: int, j: int) -> int:
            cur_l = [i, j]
            next_val = i + j
            while next_val in arr_set:
                cur_l.append(next_val)
                next_val = cur_l[-2] + cur_l[-1]

            return len(cur_l)

        res = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                l = max_fibo(arr[i], arr[j])
                res = max(res, l)
        return res if res > 2 else 0
        

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        # dp neetcode optimised?
        arr_map = {n:i for i, n in enumerate(arr)}
        res = 0
        # dp = {} # (i, j) -> length of longest subseq
        dp = [[0] * len(arr) for _ in range(len(arr))]

        for i in reversed(range(len(arr)-1)):
            for j in reversed(range(i+1, len(arr))):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2

                if nxt in arr_map:
                    length = 1 + dp[j][arr_map[nxt]]
                    res = max(res, length)
                dp[i][j] = length
        return res