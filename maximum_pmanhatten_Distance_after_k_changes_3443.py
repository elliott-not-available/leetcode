# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description/?envType=daily-question&envId=2025-06-20

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        vert = [0, 0] # up, down
        hori = [0, 0] # left, righ
        res = 0

        def cnt(d1, d2, t):
            return abs(d1-d2) + t*2

        for c in s:
            if c=="N":
                vert[0] += 1
            if c=="S":
                vert[1] += 1

            if c=="E":
                hori[1] += 1
            if c=="W":
                hori[0] += 1

            t1 = min(vert[0], vert[1], k)
            t2 = min(hori[0], hori[1], k - t1)
            res = max(res, cnt(vert[0], vert[1], t1) + cnt(hori[1], hori[0], t2))

        
        return res