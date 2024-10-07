# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/?envType=daily-question&envId=2024-10-07

class Solution:
    def minLength(self, s: str) -> int:
        substrings = ["AB", "CD"]
        i = 0
        while i <= len(s):
            # print(s, i)
            if s[i:i+2] in substrings:
                # print(s[i:i+2])
                s = s[:i] + s[i+2:]
                if i > 0:
                    i -= 1
            else:
                i += 1

        return len(s)
    
# this solution uses a different approach, would be more awkward to add new substrings to
class Solution_notmine:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c == "B" and stack[-1] == "A":
                stack.pop()
            elif c == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)