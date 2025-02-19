# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2025-02-19

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_hap = 3 * (2**(n-1))

        res = []

        # if total_hap > k:
        #     return ""
        
        choices = "abc"
        l, r = 1, total_hap

        for i in range(n):
            cur = l
            partion_size = (r - l + 1) // len(choices)

            for c in choices:
                if k in range(cur, cur + partion_size):
                    res.append(c)
                    l = cur
                    r = cur + partion_size - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partion_size

        return "".join(res)