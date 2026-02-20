# https://leetcode.com/problems/special-binary-string/description/?envType=daily-question&envId=2026-02-20

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # du sol

        cnt = 0
        res = []
        i = 0

        for j in range(len(s)):
            cnt += 1 if s[j]=="1" else -1

            if cnt==0:
                res.append("1"+self.makeLargestSpecial(s[i+1:j]) + "0")
                i=j+1

        res.sort(reverse=True)
        return "".join(res)