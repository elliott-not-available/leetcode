# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/?envType=daily-question&envId=2026-03-06

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        br = False

        for c in s:

            if c == "0" and br==False:
                br = True
                # first break

            if c == "1" and br:
                return False
                # continue segment

        # could also just check for "01" in sequence

        return True