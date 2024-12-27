# best_sightseeing_pair_1014
# https://leetcode.com/problems/best-sightseeing-pair/description/?envType=daily-question&envId=2024-12-27

class Solution:
    # bruteforce O(n^2)
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        res = 0
        cur_max = values[0] - 1

        for i in range(1, len(values)):
            res = max(res, values[i] + cur_max)
            cur_max = max(cur_max - 1, values[i] - 1)
            
        return res
        