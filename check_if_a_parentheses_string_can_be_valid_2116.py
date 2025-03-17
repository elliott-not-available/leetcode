# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/?envType=daily-question&envId=2025-01-12

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        if s[0] == ")" and locked[0] == "1" or s[-1] == "(" and locked[-1] == "1":
            return False

        l_s = [] 
        u_s = []

        for i in range(n):

            if locked[i] == "0" :
                u_s.append(i)
            elif s[i] == "(":
                l_s.append(i)
            else:
                if l_s:
                    l_s.pop()
                    continue
                elif u_s:
                    u_s.pop()
                    continue
                else:
                    return False
                
        while l_s and u_s and l_s[-1] < u_s[-1]:
            l_s.pop()
            u_s.pop()
        if l_s:
            return False
        return True