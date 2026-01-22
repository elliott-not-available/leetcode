# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/?envType=daily-question&envId=2026-01-22

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:

        # def is_sorted(inp):
        #     return inp == sorted(inp)
        
        temp = nums
        res = 0


        while (len(temp)-1)>0:
            # if is_sorted(temp):
            #     return res
            
            min_index = -1
            min_sum = float('inf')
            ascending = True

            for i in range(len(temp)-1):
                cur_sum = temp[i] + temp[i+1]

                if temp[i] > temp[i+1]:
                    ascending = False

                if cur_sum < min_sum:
                    min_index = i
                    min_sum = cur_sum

            if ascending:
                return res
                
            res += 1
            temp[min_index] = min_sum
            temp.pop(min_index+1)

        return res