# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/?envType=daily-question&envId=2025-10-27

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        def count_lasers(bin_string):
            n_devices = 0
            for c in bin_string:
                if c == "1":
                    n_devices += 1
            return n_devices
        
        res = 0
        prev = count_lasers(bank[0])

        for row in bank[1:]:
            cur_row = count_lasers(row)
            if cur_row:
                res += prev * cur_row
                prev = cur_row
        return res