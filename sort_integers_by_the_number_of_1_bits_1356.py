# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=daily-question&envId=2026-02-25

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def n_set_bits(number):
            binn = bin(number)[2:]
            # could use .bit_count() instead
            # second value is to default to ascending
            return binn.count("1"), number
        arr.sort(key=n_set_bits)
        return arr