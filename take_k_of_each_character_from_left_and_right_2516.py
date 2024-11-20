# take_k_of_each_character_from_left_and_right_2516
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/?envType=daily-question&envId=2024-11-20

from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # bruteforce + memeoiz not efficient enough (s.length can be 10^5)

        # tot = Counter(s)
        # for _, v in tot.items():
        #     if v < k:
        #         return -1

        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord("a")] += 1

        if min(count) < k:
            return -1
        
        res = float("inf")
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord("a")] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord("a")] += 1
                l += 1

            res = min(res, len(s) - (r-l+1))

        return res
        

