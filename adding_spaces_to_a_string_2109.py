# adding_spaces_to_a_string_2109
# https://leetcode.com/problems/adding-spaces-to-a-string/description/?envType=daily-question&envId=2024-12-03

class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        res = ""
        ind_space = 0
        n_space = spaces[ind_space]
        

        for i, c in enumerate(s):
            if i == n_space:
                try:
                    ind_space += 1
                    n_space = spaces[ind_space]
                except IndexError:
                    n_space = None
                res += " "

            res += c

        return res
        