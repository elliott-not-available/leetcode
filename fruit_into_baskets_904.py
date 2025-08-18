# https://leetcode.com/problems/fruit-into-baskets/description/?envType=daily-question&envId=2025-08-04
from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fruit_cnt = defaultdict(int)
        s = 0
        res = 0

        for i in range(len(fruits)):
            fruit_cnt[fruits[i]] += 1

            while len(fruit_cnt) > 2:
                fruit_cnt[fruits[s]] -= 1
                if fruit_cnt[fruits[s]] == 0:
                    del fruit_cnt[fruits[s]]
                s += 1

            res = max(res, i - s + 1)



            




        return res
        