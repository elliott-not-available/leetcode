# delete_characters_to_make_fancy_string_1957
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        new_s = s[:2]
        
        for i in range(2, len(s)):
            c = s[i]
            if new_s[-2] == new_s[-1] == c:
                continue
            new_s += c

        return new_s