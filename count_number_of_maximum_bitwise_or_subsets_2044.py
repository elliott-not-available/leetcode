# count_number_of_maximum_bitwise_or_subsets_2044
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/?envType=daily-question&envId=2024-10-18

class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n

        def dfs(i, cur_or):
            nonlocal max_or

            if i == len(nums):
                return 1 if cur_or == max_or else 0 

            return (dfs(i+1, cur_or) + dfs(i+1, cur_or | nums[i]))

        return dfs(0, 0)


