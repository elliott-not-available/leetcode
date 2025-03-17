# https://leetcode.com/problems/construct-smallest-number-from-di-string/description/?envType=daily-question&envId=2025-02-18

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # start from smallest (1), try and follow pattern
        # stack problem

        res, stack = [], []

        for i in range(len(pattern) + 1):
            stack.append(i+1)

            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    res.append(str(stack.pop()))

        return "".join(res)

