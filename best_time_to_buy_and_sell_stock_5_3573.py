# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/?envType=daily-question&envId=2025-12-17
from functools import cache
class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        # cached dfs, another solution is dp
        n = len(prices)

        @cache
        def dfs(i, j, state):
            if j ==0:
                return 0
            if i == 0:
                return (
                    0 if state==0 else -prices[0] if state==1 else prices[0]
                )

            # dfsing
            p = prices[i]

            if state==0:
                res = max(
                    dfs(i-1, j, 0), dfs(i-1, j, 1) + p, dfs(i-1, j, 2) - p
                )
            elif state==1:
                res = max(dfs(i-1, j, 1), dfs(i-1, j-1, 0) - p)
            else:
                res = max(dfs(i-1, j, 2), dfs(i-1, j-1, 0) + p)

            return res

        ans = dfs(n-1, k, 0)
        dfs.cache_clear()

        return ans
        