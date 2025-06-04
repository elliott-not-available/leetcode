# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/?envType=daily-question&envId=2025-06-04

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        # for each i compare max length word starting at i

        if numFriends == 1:
            return word

        res = ""
        N = len(word)
        max_l = N - numFriends + 1
        for i in range(N):
            
            res = max(res, word[i: i+max_l])
        return res