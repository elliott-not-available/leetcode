# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/?envType=daily-question&envId=2025-06-04

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        # use l, r pointers. left-over space = numfriends-1

        if numFriends == 1:
            return word

        res = ""
        N = len(numFriends)

        for i in range(N):
            res = max(res, word[i: min(i+N-numFriends+1, N)])
        return