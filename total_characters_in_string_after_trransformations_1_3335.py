# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/?envType=daily-question&envId=2025-05-13

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # # time_limit_exceeded
        # n_letter = {
        #     "a": "b",
        #     "b": "c",
        #     "c": "d",
        #     "d": "e",
        #     "e": "f",
        #     "f": "g",
        #     "g": "h",
        #     "h": "i",
        #     "i": "j",
        #     "j": "k",
        #     "k": "l",
        #     "l": "m",
        #     "m": "n",
        #     "n": "o",
        #     "o": "p",
        #     "p": "q",
        #     "q": "r",
        #     "r": "s",
        #     "s": "t",
        #     "t": "u",
        #     "u": "v",
        #     "v": "w",
        #     "w": "x",
        #     "x": "y",
        #     "y": "z",
        #     "z": "ab",
        # }
        # MOD = 10**9 +7
        # cnt = 0
        # cur = [c for c in s]
        # while cnt < t:
        #     cur = [n_letter[c] for c in cur]
        #     cur = "".join(cur)
        #     cnt += 1
        # return len(cur) % MOD
        ##############################################
        # might be best to directly add t?
        MOD = 10**9 + 7
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord("a")] += 1
        
        for _ in range(t):
            nxt = [0] * 26
            z = cnt[25]

            nxt[0] = z
            nxt[1] = z + cnt[0] # mod here?

            for i in range(2, 25):
                nxt[i] = cnt[i-1]
            cnt = nxt

        res = sum(cnt) % MOD
        return res
