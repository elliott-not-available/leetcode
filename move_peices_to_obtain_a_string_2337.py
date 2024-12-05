# move_peices_to_obtain_a_string_2337
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/?envType=daily-question&envId=2024-12-05

from collections import Counter

class Solution:
    def canChange(self, start: str, target: str) -> bool:

        start_q = []
        target_q = []

        for i in range(len(start)):
            if start[i] != "_":
                start_q.append((start[i],i))
            if target[i] != "_":
                target_q.append((target[i],i))

        if len(start_q) != len(target_q):
            return False
        
        while not len(start_q) == 0:
            start_c, start_i = start_q.pop(0)
            target_c, target_i = target_q.pop(0)

            if (
                start_c != target_c
                or (start_c == "L" and start_i < target_i)
                or (start_c == "R" and start_i > target_i)
            ):
                return False
        return True