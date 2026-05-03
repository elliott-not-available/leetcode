# https://leetcode.com/problems/rotate-string/description/?envType=daily-question&envId=2026-05-03

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        
        n_s = s + s
        print(n_s)
        if goal in n_s:
            return True
        return False