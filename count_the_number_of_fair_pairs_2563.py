# count_the_number_of_fair_pairs_2563
# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2024-11-13

class Solution_bruteforce:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        # 2 pntr times out
        res = 0
        n = len(nums)


        for i in range(n-1):
            if nums[i] >= upper:
                continue

            for j in range(i+1, n):

                if j <= i:
                    continue

                pair = (nums[i], nums[j])
                p_sum = pair[0] + pair[1]

                # only works if nums is sorted
                # if p_sum > upper:
                #     break

                # if p_sum < lower:
                #     continue

                if p_sum >= lower and p_sum <= upper:
                    res+=1

                # res += 1

        return res
    

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        
        def bin_search(l, r, target):
            # retrns largest i where nums[i] < target

            while l <= r:
                m = (l + r) // 2

                if nums[m] >= target:
                    r = m-1
                else:
                    l = m+1

            return r
        
        nums.sort()
        res = 0
        n = len(nums)

        for i in range(n):
            low = lower - nums[i]
            up = upper - nums[i]

            res += bin_search(i+1, n - 1, up + 1) - bin_search(i+1, n - 1, low)


        return res