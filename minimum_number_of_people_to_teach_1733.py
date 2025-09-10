# https://leetcode.com/problems/minimum-number-of-people-to-teach/?envType=daily-question&envId=2025-09-10
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        nomatch = set()

        for a, b in friendships:
            can_talk = False

            for l in languages[a-1]:
                if l in languages[b-1]:
                    can_talk = True
                    break

            if not can_talk:
                nomatch.add(a-1)
                nomatch.add(b-1)

        res = len(languages)
        for i in range(1, n+1):
            t = 0
            for p in nomatch:
                if i not in languages[p]:
                    t += 1
            res = min(res, t)

        return res