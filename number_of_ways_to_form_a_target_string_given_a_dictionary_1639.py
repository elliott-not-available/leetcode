# number_of_ways_to_form_a_target_string_given_a_dictionary_1639
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/?envType=daily-question&envId=2024-12-29

from collections import defaultdict
from functools import cache

class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        str_count = [defaultdict(int) for _ in range(len(words[0]))]
        w_len, t_len = len(words[0]), len(target)
        
        MOD = 10**9 +7

        for w in words:
            for i, c in enumerate(w):
                str_count[i][c] += 1

        @cache
        def dp(i, target_i):
            if target_i == t_len: return 1
            if i == w_len: return 0

            res = dp(i + 1, target_i)
            desired_char = target[target_i]

            if str_count[i][desired_char]:
                res += str_count[i][desired_char] * dp(i + 1, target_i + 1)

            return res % MOD


        return dp(0,0)
        