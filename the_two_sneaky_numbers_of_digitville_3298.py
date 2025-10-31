# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/?envType=daily-question&envId=2025-10-31
from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        return [c[0] for c in Counter(nums).most_common(2)]