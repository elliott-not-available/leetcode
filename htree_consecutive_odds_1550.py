# https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2025-05-11

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:

        c = 0

        for n in arr:
            if n % 2:
                c += 1
            else:
                c = 0

            if c == 3:
                return True
        return False

        