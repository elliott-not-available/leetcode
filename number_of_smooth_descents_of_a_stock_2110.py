# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/?envType=daily-question&envId=2025-12-15

class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        n = len(prices)
        res = 1
        prev = 1

        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev


        return res
        