# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/?envType=daily-question&envId=2025-06-03

from collections import deque

class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:

        n = len(status)
        can_open = [status[i]==1 for i in range(n)]
        has_box, used = [False] * n, [False] * n

        q = deque()
        res = 0


        for box in initialBoxes:
            has_box[box] = True
            if can_open[box]:
                q.append(box)
                used[box] = True
                res += candies[box]

        while q:
            big_box = q.popleft()
            for key in keys[big_box]:
                can_open[key] = True
                if not used[key] and has_box[key]:
                    q.append(key)
                    used[key] = True
                    res += candies[key]
            for box in containedBoxes[big_box]:
                has_box[box] = True
                if not used[box] and can_open[box]:
                    q.append(box)
                    used[box] = True
                    res += candies[box]


        return res
        