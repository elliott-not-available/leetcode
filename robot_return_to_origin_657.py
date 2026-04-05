# https://leetcode.com/problems/robot-return-to-origin/description/?envType=daily-question&envId=2026-04-05

class Solution:
    
    def judgeCircle(self, moves: str) -> bool:
        # could count match oposite moves
        start = [0, 0]
        conv = {
            "U":[1, 0],
            "D":[-1, 0],
            "L":[0, -1],
            "R":[0, 1],
        }

        for c in moves:
            a = conv[c]
            start[0] += a[0]
            start[1] += a[1] 

        return start==[0,0]