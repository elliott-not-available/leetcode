# https://leetcode.com/problems/apple-redistribution-into-boxes/?envType=daily-question&envId=2025-12-24

class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        
        t = sum(apple,)
        capacity.sort(reverse=True)

        i = 0
        cur = 0

        # print(capacity)
        while cur < t:
            cur += capacity[i]
            i += 1
            # print(cur, i)

        return i