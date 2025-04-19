# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2025-04-19


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:

        # # Brute force 2pntr O(n**2)
        # N = len(nums)
        # res = 0

        # for i in range(N-1):
        #     # negative values are used also
        #     # if nums[i] > upper:
        #     #     continue
        #     for j in range(i+1, N):
        #         cur_sum = nums[i] + nums[j]

        #         if lower <= cur_sum <= upper:
        #             res += 1

        # return res
        #########################################
        # # this is getting timelimit exceeded, i think i have made a silly mistake somewhere
        # print("sorting")
        # sorted_list = sorted(nums)
        # N = len(sorted_list)
        # res = 0

        # # find 
        # def lower_b(low, high, tar):
        #     while low <= high:
        #         mid = low + ((high-low)// 2)
        #         if sorted_list[mid] >= tar:
        #             high = mid + 1
        #         else:
        #             low = mid + 1
        #     return low
        # # can ignore i > j condition, because j > i = i > j
        

        # # count lower, count higher: res = total - lower - higher

        # for i in range(N-1):
        #     print("lower: ",i)
        #     # find pairs lower than lower limit
        #     l = lower_b(i+1, N-1, lower - sorted_list[i])

        #     print("higher: ",i)
        #     # find pairs lower than higher limit + 1
        #     r = lower_b(i+1, N-1, upper - sorted_list[i] + 1)
        #     res += (r - l)

        # return res
        ########################################################
        # KINDA 2pntr
        sorted_list = sorted(nums)
        N = len(sorted_list)

        def lower_b(v):
            l = 0
            r = N - 1
            res = 0

            while l < r:
                cur_sum = sorted_list[l] + sorted_list[r]

                if cur_sum < v:
                    res += r - l
                    l += 1
                else:
                    r -= 1
            return res
        
        return lower_b(upper+1) - lower_b(lower)





