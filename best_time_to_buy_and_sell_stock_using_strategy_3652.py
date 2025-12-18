# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/description/?envType=daily-question&envId=2025-12-18

class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:

        n = len(prices)
        profit_sum = [0] * (n + 1)
        price_sum = [0] * (n + 1)
        for i in range(n):
            profit_sum[i + 1] = profit_sum[i] + prices[i] * strategy[i]
            price_sum[i + 1] = price_sum[i] + prices[i]

        res = profit_sum[n]

        for i in range(k-1, n):
            l = profit_sum[i-k+1]
            r = profit_sum[n] - profit_sum[i+1]
            c = price_sum[i+1] - price_sum[i- k // 2 +1]
            res = max(res, l + c + r)
        return res