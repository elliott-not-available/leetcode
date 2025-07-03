# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=daily-question&envId=2025-07-03

class Solution:
    def kthCharacter(self, k: int) -> str:
        a = ['a']
        while len(a) < k:
            size = len(a)
            for i in range(size):
                nxt_c = chr(ord("a") + ((ord(a[i]) - ord("a") + 1)% 26))
                a.append(nxt_c)


        return a[k - 1]