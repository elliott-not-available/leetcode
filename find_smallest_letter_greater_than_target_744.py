# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/?envType=daily-question&envId=2026-01-31

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        # for i in range(len(letters)-1, -1, -1):
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        return letters[0]