# https://leetcode.com/problems/shifting-letters-ii/description/?envType=daily-question&envId=2025-01-05

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        # original solution:
        # function shifter -> shifts a character by amount (uses ord() and chr())
        # collect amount each index is shifted
        # shift each string index by amount index
        # timeout - too slow

        def shifter(letter: str, amount: int) -> str:
            base = 97
            MOD = 26

            n = ord(letter)
            nn = n - base

            res = (nn + amount) % MOD

            return chr(base + res)

        cur_str = [c for c in s]
        amount = [0]*len(s)

        for shift in shifts:

            start, end, direction = shift
            if direction == 0:
                direction = -1

            for i in range(start, end+1):
                amount[i] += direction

        for i in range(len(s)):
            cur_str[i] = shifter(cur_str[i], amount[i])

        return "".join(cur_str)
        

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)
        MOD = 26

        for l, r, diff in shifts:
            prefix_diff[r+1] += 1 if diff else -1
            prefix_diff[l] += -1 if diff else 1

        diff = 0
        cur_str = [ord(c)-ord("a") for c in s]
        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            cur_str[i-1] = (diff + cur_str[i-1]) % MOD

        s = [chr(ord("a") + n) for n in cur_str]
        return "".join(s)
