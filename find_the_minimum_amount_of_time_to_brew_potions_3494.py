# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/?envType=daily-question&envId=2025-10-09

class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:

        n = len(skill)
        res = [0] * n

        for j in range(len(mana)):
            cur_time = 0

            for i in range(n):
                cur_time = max(cur_time, res[i]) + skill[i]*mana[j]
            res[n-1] = cur_time

            for i in range(n-2, -1, -1):
                res[i] = res[i+1] - skill[i+1]*mana[j]


        return res[n-1]