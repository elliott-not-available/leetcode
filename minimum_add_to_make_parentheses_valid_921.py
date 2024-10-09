# minimum_add_to_make_parentheses_valid_921
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2024-10-09

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # ah this doesnt work because you gotta respect order
        # a = s.count('(')
        # b = s.count(')')
        a_count, b_count = 0, 0
        for c in s:
            if c == '(':
                # needs a match
                a_count += 1
            if c == ')':
                if a_count >= 1:
                    # found a match
                    a_count -= 1
                else:
                    # needs a match
                    b_count += 1    

        return a_count + b_count

