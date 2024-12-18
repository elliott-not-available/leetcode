# final_prices_with_a_special_discount_in_a_shop_1475
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/?envType=daily-question&envId=2024-12-18

class Solution:
    # bruteforce og solution
    def finalPrices(self, prices: list[int]) -> list[int]:
        N = len(prices)
        res = [None] * N

        for i in range(N-1):
            val = prices[i]
            j = i + 1
            while res[i] == None and j < N:
                if prices[j] <= val:
                    res[i] = val - prices[j]
                j += 1
            if res[i] == None:
                res[i] = prices[i]
                
        res[-1] = prices[-1]

        return res
    


class Solution:
    # using monotonic increasing stack
    def finalPrices(self, prices: list[int]) -> list[int]:
        
        res = [p for p in prices]

        stack = []

        for i in range(len(prices)):

            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]

            stack.append(i)

        return res