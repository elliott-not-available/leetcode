# count_ways_to_build_good_strings_2466
# https://leetcode.com/problems/count-ways-to-build-good-strings/description/?envType=daily-question&envId=2024-12-30

from functools import cache

class Solution:
    # backtracking? with cache, O(2**high)
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        MOD = 10**9 +7

        @cache
        def dfs(length):
            if length > high:
                return 0
            res = 1 if length >= low else 0
            res += dfs(length + zero) + dfs(length + one)
            return res % MOD
        return dfs(0)