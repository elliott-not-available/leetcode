# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/?envType=daily-question&envId=2026-04-15

class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        # # index not working
        # t = words.index(target)
        # n = len(words)
        # res = min(n, abs(t - startIndex), n-abs(t-startIndex))
        # return res if res < n else -1

        n = len(words)

        for i in range(2*n):
            if ((words[(startIndex+i) % n] == target) |
                (words[(startIndex-i) % n] == target)):
                return i
        return -1