# https://leetcode.com/problems/ones-and-zeroes/description/?envType=daily-question&envId=2025-11-11

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        d = {(0,0):0}

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            new_d = dict(d)

            for (z, o), cur in d.items():
                new_z, new_o = z + zeros, o + ones

                if new_z <= m and new_o <= n:
                    new_d[(new_z, new_o)] = max(new_d.get((new_z, new_o), 0), cur + 1)

            dp = new_d

        return max(dp.values())