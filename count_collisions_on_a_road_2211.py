# https://leetcode.com/problems/count-collisions-on-a-road/description/?envType=daily-question&envId=2025-12-04

class Solution:
    def countCollisions(self, directions: str) -> int:

        directions = directions.lstrip("L")
        # print(directions)
        directions = directions.rstrip("R")

        # print(directions)

        res = 0

        for c in directions:
            if c == "S":
                continue
            else:
                res += 1
            
        return res