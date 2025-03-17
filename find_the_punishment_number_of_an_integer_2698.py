# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/?envType=daily-question&envId=2025-02-15

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def is_valid(i: int, cur: int, target: int, string: str) -> bool:
            if i == len(string) and cur == target:
                return True
            
            for j in range(i, len(string)):
                s = string[i:j+1]
                if is_valid(j+1, cur + int(s), target, string):
                    return True
            return False
            # i have missunderstood this - i think splitting and seeing if they add (recursive) is the answer
            # for char in str(square):
            #     ss += int(char)
            # return i == ss 
        # 


        res = 0
        for i in range(1, n + 1):
            sqr = i*i
            if is_valid(0, 0, i, str(sqr)):
                res += sqr

        return res