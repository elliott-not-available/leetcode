# https://leetcode.com/problems/furthest-point-from-origin/?envType=daily-question&envId=2026-04-24
from collections import Counter
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = Counter(moves)

        return abs(c["R"] - c["L"]) + c["_"]