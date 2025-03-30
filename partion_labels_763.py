# https://leetcode.com/problems/partition-labels/description/?envType=daily-question&envId=2025-03-30

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        res = []

        last_ind = {c:i for i, c in enumerate(s)}
        r = last_ind[s[0]]
        size = 1

        for i, c in enumerate(s):


            if last_ind[c] > r:
                r = last_ind[c]

            if i == r:
                res.append(size)
                size = 0
                if i != len(s) - 1:
                    r = last_ind[s[i+1]]
            size += 1
        
        return res