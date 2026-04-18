# https://leetcode.com/problems/mirror-distance-of-an-integer/description/?envType=daily-question&envId=2026-04-18

class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = str(n)[::-1]
        mir_dist = abs(n - int(rev))
        return mir_dist