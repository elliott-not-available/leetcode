# https://leetcode.com/problems/fruits-into-baskets-ii/?envType=daily-question&envId=2025-08-05

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for f in fruits:
            leftover = 1
            for i in range(len(baskets)):
                if baskets[i] >= f:
                    baskets[i] = 0
                    leftover = 0
                    break
            res += leftover

        return res