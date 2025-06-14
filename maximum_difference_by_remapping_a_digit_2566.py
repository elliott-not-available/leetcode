# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/?envType=daily-question&envId=2025-06-14
from collections import Counter

class Solution:
    def minMaxDifference(self, num: int) -> int:

        # c = Counter([int(s) for s in str(num)])

        maxi = 0
        mini = num
        max_vis = set()
        min_vis = set()
        str_num = str(num)

        for c in str_num:
            if c not in max_vis:
                max_vis.add(c)
                tmp = str_num
                temp_max = int(tmp.replace(c, '9'))
                maxi =  max(maxi, temp_max)

            if c not in min_vis:
                min_vis.add(c)
                temp = str_num
                temp_min = int(temp.replace(c, '0'))
                mini = min(mini, temp_min)

        return maxi - mini