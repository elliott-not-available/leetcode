# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2025-02-02

class Solution:
    def check(self, nums: list[int]) -> bool:
        max_num = max(nums)
        pre = nums[0]
        shifts = 0

        for num in nums[1:]:
            
            # check current number is >= previous
            if num >= pre:
                pre = num
                continue
            else:
                # if shifted
                if pre == max_num and shifts == 0:
                    shifts = 1
                    pre = num
                else:
                    return False
            
        # check reach around
        if nums[-1] != max_num:
            return nums[0] >= nums[-1]
            
        return True
    

class Solution_neet:
    def check(self, nums: list[int]) -> bool:
        # smart out of the box thinking

        N = len(nums)
        count = 1

        for i in range(1, 2 * N):
            if nums[(i -1) % N] <= nums[i % N]:
                count +=1
            else:
                count = 1
            if count == N:
                return True
            
        return N == 1