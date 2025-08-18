# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2025-08-14

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur = '\0'
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:

                cur = max(num[i], cur)


        return "" if cur == "\0" else cur*3