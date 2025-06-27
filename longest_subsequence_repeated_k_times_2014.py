# https://leetcode.com/problems/longest-subsequence-repeated-k-times/description/?envType=daily-question&envId=2025-06-27

from collections import Counter, deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ""
        candidate = sorted(
            [c for c, w in Counter(s).items() if w >= k], reverse=True
        )

        q = deque(candidate)

        while q:
            curr = q.popleft()
            if len(curr) > len(res):
                res = curr

            for ch in candidate:
                nxt = curr + ch
                it = iter(s)

                if all(ch in it for ch in nxt*k):
                    q.append(nxt)

        return res
    