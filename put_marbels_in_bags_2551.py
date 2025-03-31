# https://leetcode.com/problems/put-marbles-in-bags/description/?envType=daily-question&envId=2025-03-31
# from heapq import heappush
class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:

        if k == 1:
            return 0

        split_costs = []

        for i in range(len(weights)-1):
            split_cost = int(weights[i]) + int(weights[i+1])
            # heappush(split_costs, split_cost)
            split_costs.append(split_cost)


        split_costs.sort()
        n_splits = k - 1
        min_cost = sum(split_costs[:n_splits])
        max_cost = sum(split_costs[-n_splits:])

        print(split_costs)
        print(f"{min_cost}, {max_cost}")


        return max_cost - min_cost