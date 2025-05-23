# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/?envType=daily-question&envId=2025-05-23

class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        # greedy

        s = 0
        res = []

        # build cur sum with 0 ops and ^ diff array
        for x in nums:
            s += x
            y = x ^ k
            res.append(y - x)

        # sort so largest diff are first
        res.sort(reverse=True)

        # for every other item check if they are larger than 0
        # if so add to sum
        for i in range(0, len(res) - 1, 2):

            if res[i] + res[i+1] <= 0:
                break

            s += res[i] + res[i+1]

        
        return s
        