# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=daily-question&envId=2026-03-03

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s):
            res = ""
            for c in s:
                if c =="1": 
                    res+="0"
                if c=="0":
                    res+="1"

            return res
        
        cur = "0"

        for _ in range(1, n):
            cur = cur + "1" + invert(cur)[::-1]

            # if len(cur) >= k-1:
            #     return cur[k-1]


        return cur[k-1]