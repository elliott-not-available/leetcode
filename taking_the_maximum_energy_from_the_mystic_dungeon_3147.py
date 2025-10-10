# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/?envType=daily-question&envId=2025-10-10

class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        res = -1000
        n = len(energy)

        for i in range(n-k, n):
            
            # print(i)
            # print(energy[i::-k])
            # res = max(res, sum(energy[i::-k]))
            cur_total = 0
            j=i
            while j>=0:
                cur_total += energy[j]
                res = max(res, cur_total)
                j -=k
        return res