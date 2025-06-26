# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/?envType=daily-question&envId=2025-06-26

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        sm = 0
        cnt = 0 
        buts = k.bit_length()

        for i, ch in enumerate(s[::-1]):
            if ch == "1":
                if i < buts and sm + (1 << i) <= k:
                    sm += 1 << i
                    cnt += 1

            else:
                cnt += 1

        return cnt
        