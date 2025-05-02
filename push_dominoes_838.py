# https://leetcode.com/problems/push-dominoes/?envType=daily-question&envId=2025-05-02

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        dirs = [(i, d) for i, d in enumerate(dominoes) if d != "." ]
        dirs = [(-1, "L")] + dirs + [(N, "R")]
        res = list(dominoes)

        for h in range(len(dirs)-1):
            i, x = dirs[h]
            j, y = dirs[h+1]

            if x == y:
                for k in range(i+1, j):
                    res[k] = x
            # right - left
            elif x > y: 
                for k in range(i+1, j):
                    if k - i > j - k:
                        res[k] = "L"
                    elif k - i < j - k:
                        res[k] = "R"
                    else:
                        res[k] = "."

        return "".join(res)