# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2025-10-25
class Solution:
    def totalMoney(self, n: int) -> int:

        # # shit brute force
        # res = 0

        # for i in range(1, n+1):
        #     tmp = i-1
        #     mod_component = tmp % 7
        #     if mod_component == 0:
        #         mod_component = 7
        #     a = (tmp % 7) + (tmp // 7) +1
        #     print(a)
        #     res += a
        # return res
        n_weeks = n // 7
        base_week_total = 28

        tmax = 28 + (n_weeks-1)*7
        summ = n_weeks * (base_week_total + tmax) // 2

        last_week_monday = 1 + n_weeks
        last_biddies = 0

        for day in range(n % 7):
            last_biddies += last_week_monday + day

        return summ + last_biddies