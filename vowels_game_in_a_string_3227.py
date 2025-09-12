# https://leetcode.com/problems/vowels-game-in-a-string/?envType=daily-question&envId=2025-09-12

class Solution:
    def doesAliceWin(self, s: str) -> bool:

        vowels = "aeiou"
        cnt = 0
        for c in s:
            if c in vowels:
                cnt += 1

        if cnt == 0: return False
        if cnt % 2: return True

        # if it is even she also wins lol


        return True