# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/?envType=daily-question&envId=2025-10-20

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:

        mp = {
            "++X": +1,
            "X++": +1,
            "--X": -1,
            "X--":-1,
        }

        res = 0

        for op in operations:
            res = res + mp[op]

        return res
        