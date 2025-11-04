# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/?envType=daily-question&envId=2025-11-04
from collections import Counter
class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        res = []
        for i in range(len(nums)-k+1):
            window = nums[i:i+k]

            all_c = Counter(window).most_common()
            c = sorted(all_c, key=lambda y: (-y[1], -y[0]))

            xsum = sum(n*m for n,m in c[:x])
            res.append(xsum)

        return res
        