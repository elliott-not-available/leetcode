# https://leetcode.com/problems/avoid-flood-in-the-city/?envType=daily-question&envId=2025-10-07
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        # couldnt understand question
        res = [1] * len(rains)
        sl = SortedList()
        dic = {}

        for i, rain in enumerate(rains):

            if rain == 0:
                sl.add(i)
            else:
                res[i] = -1
                if rain in dic:
                    it = sl.bisect(dic[rain])
                    if it == len(sl):
                        return []
                    res[sl[it]] = rain
                    sl.discard(sl[it])
                dic[rain] = i
        return res