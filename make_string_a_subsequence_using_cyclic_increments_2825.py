# make_string_a_subsequence_using_cyclic_increments_2825
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description/?envType=daily-question&envId=2024-12-04

from collections import defaultdict

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        def shift_up(char: str) -> str:
            if char == "z":
                return "a"
            return chr(ord(char) + 1)


        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            if str2[j] == str1[i] or str2[j] == shift_up(str1[i]):
                j += 1

            i += 1

        return j == len(str2)

        
