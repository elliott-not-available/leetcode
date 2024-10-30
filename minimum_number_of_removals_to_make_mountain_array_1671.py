# minimum_number_of_removals_to_make_mountain_array_1671
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        # neeted
        # longest increasing subsequence: LIS

        n = len(nums)

        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)

        lds = [1] * n
        for l in reversed(range(n)):
            for m in range(l+1, n):
                if nums[m] < nums[l]:
                    lds[l] = max(lds[l], lds[m] + 1)

        result = n
        for k in range(1,n-1):
            if min(lis[k], lds[k]) > 1:
                result = min(result, n - lis[k] - lds[k] + 1)

        return result