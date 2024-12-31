# minimum_cost_for_tickets_983
# https://leetcode.com/problems/minimum-cost-for-tickets/description/?envType=daily-question&envId=2024-12-31
from functools import cache
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        # tree with three options. each cost with i moving by amount of cost, min res (3 branch recursion)
        # def dfs(i, cur_cost):
        #     if i >= len(days):
        #         return cur_cost
            
        #     # 1
        #     t1 = cur_cost + costs[0]
        #     m1 = dfs(i + 1, t1)

        #     # 7
        #     new_i = i
        #     while days[new_i] < days[i] + 7:
        #         new_i += 1
        #     t2 = cur_cost + costs[1]
        #     m2 = dfs(new_i, t2)

        #     # 30
        #     new_i = i
        #     while days[new_i] < days[i] + 30:
        #         new_i += 1
        #     t3 = cur_cost + costs[2]
        #     m3 = dfs(new_i, t3)

        #     return min(m1,m2,m3)
        durations = [1, 7, 30]

        @cache
        def dfs(i):
            if i == len(days):
                return 0
            
            res = float("inf")

            for cost, dur in zip(costs, durations):
                j = i
                while j < len(days) and days[j] < days[i] + dur:
                    j += 1
                res = min(res, cost + dfs(j))

            return res

        
        return dfs(0)
        