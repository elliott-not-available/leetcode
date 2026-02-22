# https://leetcode.com/problems/binary-gap/?envType=daily-question&envId=2026-02-22

class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        prev = None
        bin_n = bin(n)[2:]

        j=0
        while not prev and j<len(bin_n):
            if bin_n[j]=="1":
                prev = j
                break
            j+=1

        print(bin_n, prev)

        for i in range(prev, len(bin_n)):

            if bin_n[i]=="1":
                max_gap=max(max_gap, i-prev)
                prev = i

        return max_gap
