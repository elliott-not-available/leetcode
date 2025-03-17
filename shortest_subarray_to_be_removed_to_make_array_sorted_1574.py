# shortest_subarray_to_be_removed_to_make_array_sorted_1574
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/?envType=daily-question&envId=2024-11-15


class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        # Prefix
        n = len(arr)
        r = n-1
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        res = r

        l = 0
        while l < r:

            while r < n and arr[l] > arr[r]:
                r+=1
            res = min(res, r-l-1)

            if arr[l] > arr[l+1]:
                break
            l+=1
        return res