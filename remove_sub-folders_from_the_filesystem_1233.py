# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/?envType=daily-question&envId=2025-07-19

class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        res = [folder[0]]

        for i in range(1, len(folder)):
            lf = res[-1] + "/"

            if not folder[i].startswith(lf):
                res.append(folder[i])



        return res
        