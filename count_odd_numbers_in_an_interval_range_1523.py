# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/?envType=daily-question&envId=2025-12-07

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        h = (high+1)//2
        l = (low)//2

        return h - l